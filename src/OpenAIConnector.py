def get_APIKey():
    with open('./../../.secret/OpenAI_API_key.txt','r') as f:
        return ((f.read().split('\n')[-1].split(':')[1]).strip())