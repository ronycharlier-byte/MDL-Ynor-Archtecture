$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$dist = Join-Path $root "_CLOUD_EXPORTS"
$stagingFull = Join-Path $dist "full_staging"
$stagingSafe = Join-Path $dist "safe_staging"
$fullZip = Join-Path $dist "MDL_Ynor_Architecture_cloud_full.zip"
$safeZip = Join-Path $dist "MDL_Ynor_Architecture_cloud_safe.zip"
$manifest = Join-Path $dist "cloud_export_manifest.json"

function Reset-Dir {
    param([string]$Path)
    if (Test-Path $Path) {
        Remove-Item -Recurse -Force $Path
    }
    New-Item -ItemType Directory -Path $Path | Out-Null
}

function Copy-Tree {
    param(
        [string]$Destination,
        [string[]]$ExcludeDirs,
        [string[]]$ExcludeFiles
    )

    Get-ChildItem -Path $root -Force | Where-Object {
        $_.Name -ne "_CLOUD_EXPORTS" -and
        $_.Extension -ne ".zip"
    } | ForEach-Object {
        $target = Join-Path $Destination $_.Name
        if ($_.PSIsContainer) {
            Copy-Item -Path $_.FullName -Destination $target -Recurse -Force
        } else {
            Copy-Item -Path $_.FullName -Destination $target -Force
        }
    }

    foreach ($dirName in $ExcludeDirs) {
        Get-ChildItem -Path $Destination -Recurse -Directory -Force -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -eq $dirName } |
            ForEach-Object { Remove-Item -Recurse -Force $_.FullName }
    }

    foreach ($filePattern in $ExcludeFiles) {
        Get-ChildItem -Path $Destination -Recurse -File -Force -ErrorAction SilentlyContinue -Filter $filePattern |
            ForEach-Object { Remove-Item -Force $_.FullName }
    }
}

function New-Zip {
    param(
        [string]$SourceDir,
        [string]$ZipPath
    )

    if (Test-Path $ZipPath) {
        Remove-Item -Force $ZipPath
    }

    Compress-Archive -Path (Join-Path $SourceDir "*") -DestinationPath $ZipPath -CompressionLevel Optimal
}

New-Item -ItemType Directory -Path $dist -Force | Out-Null
Reset-Dir -Path $stagingFull
Reset-Dir -Path $stagingSafe

Copy-Tree -Destination $stagingFull -ExcludeDirs @() -ExcludeFiles @()
Copy-Tree -Destination $stagingSafe -ExcludeDirs @(
    ".git",
    ".venv",
    ".uv-cache",
    ".pytest_cache",
    "__pycache__",
    "logs"
) -ExcludeFiles @(
    ".env",
    "secrets.local.json",
    "*.pyc"
)

New-Zip -SourceDir $stagingFull -ZipPath $fullZip
New-Zip -SourceDir $stagingSafe -ZipPath $safeZip

$fullSize = (Get-Item $fullZip).Length
$safeSize = (Get-Item $safeZip).Length

$manifestData = [PSCustomObject]@{
    generated_at = (Get-Date).ToString("s")
    source_root = $root
    full_zip = $fullZip
    safe_zip = $safeZip
    full_zip_size_bytes = $fullSize
    safe_zip_size_bytes = $safeSize
    excluded_from_safe = [PSCustomObject]@{
        directories = @(".git", ".venv", ".uv-cache", ".pytest_cache", "__pycache__", "logs")
        files = @(".env", "secrets.local.json", "*.pyc")
    }
}

$manifestData | ConvertTo-Json -Depth 5 | Set-Content -Path $manifest -Encoding UTF8

Write-Output "Full archive: $fullZip"
Write-Output "Safe archive: $safeZip"
Write-Output "Manifest: $manifest"
