class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 7757454
    API_HASH = "0ce18cca262403f63d2975c0a2b47633"

    CASH_API_KEY = "5J46LIS7I8AA100O"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://avnadmin:AVNS_jlddRHTYTyqvWMT0wh1@pg-1aab18ba-avneeshsingh02556-3d5d.l.aivencloud.com:17011/defaultdb?sslmode=require"  # A sql database url from https://aiven.io/ Create As Database postgresql

    EVENT_LOGS = (-1002278171251)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://coderavi69:y674HbUMMDsKWl0v@cluster0.jyrtt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://i.ibb.co/hW0rkXH/Mia-Bot-logo-with-the-name-in-black-and-color.jpg"

    SUPPORT_CHAT = "testkoio"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6113096948:AAFWNDZGbcfRK0FWdObLuD60UDDqadNrTKw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "http://api.timezonedb.com/v2.1/get-time-zone"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5217960660  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
