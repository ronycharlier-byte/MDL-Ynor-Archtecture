import json

file_path = r"c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\_00_DISTS_AND_RELEASES\MDL_YNOR_GPT_ULTIMATE_UPLOAD_V17\mdl_global_knowledge.json"
paypal_link = "https://www.paypal.com/ncp/payment/BDTWYYEN8XMML"

try:
 with open(file_path, 'r', encoding='utf-8') as f:
 content = f.read()

 # Replace the placeholder with the real link
 new_content = content.replace("[VOTRE_LIEN_PAYPAL_ME]", paypal_link)

 with open(file_path, 'w', encoding='utf-8') as f:
 f.write(new_content)
 
 print("Real PayPal link successfully injected into JSON.")
except Exception as e:
 print(f"Error: {e}")
