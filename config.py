from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "bbdd206f92e1ca4bc4935b43dfd4a2a1")
      API_ID = int(getenv("API_ID", "20836266"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8059053048:AAFL13zFN1r39295jQNpYE58uln1hsE5Zoo")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002448891440:-1002193512220").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
