import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7724944994:AAHd-eskJmePbPQsuRD3sEmKowAkC0kWqKs")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26258063"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "be0a0e2ecd938bfc5401d35a399deeb7")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://zuuvou:XNWdDOsGFprx7Cnw@clusterop.pnyvj.mongodb.net/?retryWrites=true&w=majority")
