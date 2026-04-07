import json
import re

file_path = r"c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\_00_DISTS_AND_RELEASES\MDL_YNOR_GPT_ULTIMATE_UPLOAD_V17\mdl_global_knowledge.json"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update system_meta with Payment Gateway
    if 'system_meta' not in data:
        data['system_meta'] = {}
    
    if 'security_protocols' not in data['system_meta']:
        data['system_meta']['security_protocols'] = {}

    data['system_meta']['security_protocols']['PAYMENT_GATEWAY'] = "[VOTRE_LIEN_PAYPAL_ME]"
    data['system_meta']['security_protocols']['ACTIVATION_PROCEDURE'] = "Automatic issuance of L0 Expert Key upon PayPal confirmation."

    # 2. Update previews to point to PayPal instead of Stripe or others
    def update_previews(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'preview' and isinstance(v, str):
                    # Replace Stripe links or generic payment text with PayPal placeholder
                    v = re.sub(r'https://buy\.stripe\.com/\w+', '[VOTRE_LIEN_PAYPAL_ME]', v)
                    v = re.sub(r'\[LIEN_PAYPAL\]', '[VOTRE_LIEN_PAYPAL_ME]', v)
                    v = re.sub(r'\[VOTRE_LIEN_STRIPE\]', '[VOTRE_LIEN_PAYPAL_ME]', v)
                    obj[k] = v
                else:
                    update_previews(v)
        elif isinstance(obj, list):
            for item in obj:
                update_previews(item)

    update_previews(data)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("PayPal integration and Stripe replacement completed in JSON.")
except Exception as e:
    print(f"Error: {e}")
