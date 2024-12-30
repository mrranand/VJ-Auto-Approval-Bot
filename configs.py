# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28440645"))
    API_HASH = getenv("API_HASH", "b9d450c3bf3d213c3a0152f1b712f29e")
    BOT_TOKEN = getenv("BOT_TOKEN", "8050387802:AAEczBd_3nzGH4I56Tfqn8fQuIQ2z0XA-zc")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002159944048")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "7204831423").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://techanand9920:ERkZZKx9tGUCNZat@cluster0.n1knp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
