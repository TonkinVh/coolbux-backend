while True:
    import pathlib

    from google.oauth2 import id_token
    from pip._vendor import cachecontrol
    from weblib import google

    try:
        maitenance = False
        canpayout = True
        from gevent import monkey;

        monkey.patch_all()
        import hashlib, uuid
        from flask import send_from_directory, render_template
        from flask_cors import CORS
        from flask import Flask, request, session, jsonify, make_response, redirect
        import flask, random, requests, json, time, subprocess
        import datetime, secrets
        from flask import send_file, abort
        import time, os, sys, re
        from io import BytesIO
        from bit import PrivateKey
        from bit import Key
        from zxcvbn import zxcvbn
        import smtplib, nltk
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from google_auth_oauthlib.flow import Flow
        import statistics
        from flask_limiter import Limiter
        from flask_limiter.util import get_remote_address
        from requests.structures import CaseInsensitiveDict
        import numpy as np
        from PIL import Image
        import cv2, io
        from hashlib import sha256
        import socket, jpysocket


        def is_google(function):
            def wrapper(*args, **kwargs):
                if "google_id" not in session:
                    return redirect("http://www.easycaptchas.coolbux.live", code=302)
                else:
                    return (function)

            return wrapper


        def CalculateReward(waves):
            if int(waves) == 1:
                return (0.1)
            elif int(waves) == 2:
                return (0.105)
            elif int(waves) == 3:
                return (0.11)
            elif int(waves) == 4:
                return (0.12)
            else:
                return (0.125)


        def most_frequent(List):
            counter = 0
            num = List[0]

            for i in List:
                curr_frequency = Liaast.count(i)
                if (curr_frequency > counter):
                    counter = curr_frequency
                    num = i

            return num


        def Difficulty(waves):
            if int(waves) < 5:
                return ("Easy")

            elif int(waves) > 4:
                if int(waves) > 9:
                    return ("Hard")
                else:
                    return ("Medium")


        client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secrets.json")
        GOOGLE_CLIENT_ID = "884745994664-mbddq041oos76tdppmfhm0fo7fa07unj.apps.googleusercontent.com"
        flow = Flow.from_client_secrets_file(client_secrets_file=client_secrets_file,
                                             scopes=["https://www.googleapis.com/auth/userinfo.profile",
                                                     "https://www.googleapis.com/auth/userinfo.email", "openid"],
                                             redirect_uri="https://easycaptchas.coolbux.live/easycaptcha/callback"
                                             )

        proxylistprivate = open("proxies.bin", 'r').read().split('\n')
        fits = open('fits.bin', 'r').read().split('\n')


        def SendMail(senderaddress, senderpassword, reciever, body, subject):
            try:
                receiver_address = reciever
                mail_content = body
                # The mail addresses and password
                sender_address = senderaddress
                sender_pass = senderpassword
                # Setup the MIME
                message = MIMEMultipart()
                message['From'] = sender_address
                message['To'] = receiver_address
                message['Subject'] = subject  # The subject line
                # The body and the attachments for the mail
                message.attach(MIMEText(mail_content, 'plain'))
                # Create SMTP session for sending the mail
                session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
                session.starttls()  # enable security
                session.login(sender_address, sender_pass)  # login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
                return ("Sent")
            except Exception as error:
                return (f"Failed*{error}")


        def percent(expression):
            if "%" in expression:
                expression = expression.replace("%", "/100")
            return eval(expression)


        def PendingVault(user):
            total = 0
            for transaction in os.listdir("Database\\PendRBX\\Kiwi"):
                if transaction.split(":")[2] == user:
                    total += float(transaction.split(":")[0])

            return (total)


        def GetTransVault(user, amount):
            total = 0
            for transaction in os.listdir("Database\\PendRBX\\Kiwi"):
                if transaction.split(":")[2] == user:
                    # get transaction
                    if float(transaction.split(":")[0]) == float(amount):
                        return (transaction)
                else:
                    pass


        users = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "AaronJames", "Aarron", "Aaryan", "Aaryn", "Aayan",
                 "Aazaan",
                 "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul",
                 "AbdulAziz",
                 "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "AbdulMajeed", "Abdulmalik",
                 "AbdulRehman", "Abdur", "Abdurraheem", "AbdurRahman", "AbdurRehmaan", "Abel", "Abhinav", "Abhisumant",
                 "Abid",
                 "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam", "AdamJames", "Addison", "Addisson",
                 "Adegbola",
                 "Adegbolahan", "Aden", "Adenn", "Adie", "Adil", "Aditya", "Adnan", "Adrian", "Adrien", "Aedan",
                 "Aedin",
                 "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed", "AhmedAziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan",
                 "Aiden",
                 "AidenJack", "AidenVee", "Aidian", "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas",
                 "Airlie", "AJ", "Ajay", "AJay", "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair",
                 "Alastair", "Alber", "Albert", "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander",
                 "Aleksandr", "Aleksandrs", "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei",
                 "Alexx",
                 "Alexzander", "Alf", "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "AlHassan", "Ali", "Aliekber",
                 "Alieu",
                 "Alihaider", "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan",
                 "AllanLaiton",
                 "Allen", "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas",
                 "Amaan",
                 "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer",
                 "Amolpreet",
                 "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs", "Andrew",
                 "Andy",
                 "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet", "Annan", "Anndra",
                 "Anselm", "Anthony", "AnthonyJohn", "Antoine", "Anton", "Antoni", "Antonio", "Antony", "Antonyo",
                 "Anubhav",
                 "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep", "Arann", "Aray", "Arayan",
                 "Archibald",
                 "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez", "Aref", "Arfin", "Argyle", "Argyll", "Ari",
                 "Aria",
                 "Arian", "Arihant", "Aristomenis", "Aristotelis", "Arjuna", "Arlo", "Armaan", "Arman", "Armen",
                 "Arnab",
                 "Arnav", "Arnold", "Aron", "Aronas", "Arran", "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur",
                 "Artur", "Arturo", "Arun", "Arunas", "Arved", "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa",
                 "Asfhan",
                 "Ash", "Ashleejay", "Ashley", "Ashton", "AshtonLloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam",
                 "Asrar",
                 "Ata", "Atal", "Atapattu", "Ateeq", "Athol", "Athon", "AthosCarlos", "Atli", "Atom", "Attila", "Aulay",
                 "Aun",
                 "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan",
                 "Ayan",
                 "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub", "Ayyub",
                 "Azaan",
                 "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise", "Babur", "Bader",
                 "Badr",
                 "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley", "Balian", "Banan", "Barath",
                 "Barkley",
                 "Barney", "Baron", "Barrie", "Barry", "Bartlomiej", "Bartosz", "Basher", "Basile", "Baxter", "Baye",
                 "Bayley",
                 "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz", "Benedict", "Benjamin", "Benjamyn", "Benji",
                 "Benn",
                 "Bennett", "Benny", "Benoit", "Bentley", "Berkay", "Bernard", "Bertie", "Bevin", "Bezalel",
                 "Bhaaldeen",
                 "Bharath", "Bilal", "Bill", "Billy", "Binod", "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake",
                 "Blazej", "Blazey", "Blessing", "Blue", "Blyth", "Bo", "Boab", "Bob", "Bobby", "BobbyLee", "Bodhan",
                 "Boedyn",
                 "Bogdan", "Bohbi", "Bony", "Bowen", "Bowie", "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley",
                 "Bradlie", "Bradly", "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan", "Branden",
                 "Brandon",
                 "Brandonlee", "BrandonLee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan",
                 "Brehme",
                 "Brendan", "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie",
                 "Brody",
                 "Brogan", "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan",
                 "Bryce",
                 "Bryden", "Brydon", "BrydonCraig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak", "Burhan",
                 "Butali",
                 "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan", "Caedyn", "Cael",
                 "Caelan",
                 "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Caiden", "CaidenPaul", "Caidyn", "Caie",
                 "Cailaen",
                 "Cailean", "CailebJohn", "Cailin", "Cain", "Caine", "Cairn", "Cal", "Calan", "Calder", "Cale",
                 "Calean",
                 "Caleb", "Calen", "Caley", "Calib", "Calin", "Callahan", "Callan", "CallanAdam", "Calley", "Callie",
                 "Callin",
                 "Callum", "Callun", "Callyn", "Calum", "CalumJames", "Calvin", "Cambell", "Camerin", "Cameron",
                 "Campbel",
                 "Campbell", "Camron", "Caolain", "Caolan", "Carl", "Carlo", "Carlos", "Carrich", "Carrick", "Carson",
                 "Carter",
                 "Carwyn", "Casey", "Casper", "Cassy", "Cathal", "Cator", "Cavan", "Cayden", "CaydenRobert",
                 "CaydenTiamo",
                 "Ceejay", "Ceilan", "Ceiran", "Ceirin", "Ceiron", "Cejay", "Celik", "Cephas", "Cesar", "Cesare",
                 "Chad",
                 "Chaitanya", "ChangHa", "Charles", "Charley", "Charlie", "Charly", "Chase", "Che", "Chester", "Chevy",
                 "Chi",
                 "Chibudom", "Chidera", "Chimsom", "Chin", "Chintu", "Chiqal", "Chiron", "Chris", "ChrisDaniel",
                 "Chrismedi",
                 "Christian", "Christie", "Christoph", "Christopher", "ChristopherLee", "Christy", "Chu", "Chukwuemeka",
                 "Cian",
                 "Ciann", "Ciar", "Ciaran", "Ciarian", "Cieran", "Cillian", "Cillin", "Cinar", "CJ", "CJay", "Clark",
                 "Clarke",
                 "Clayton", "Clement", "Clifford", "Clyde", "Cobain", "Coban", "Coben", "Cobi", "Cobie", "Coby",
                 "Codey",
                 "Codi", "Codie", "Cody", "CodyLee", "Coel", "Cohan", "Cohen", "Colby", "Cole", "Colin", "Coll", "Colm",
                 "Colt",
                 "Colton", "Colum", "Colvin", "Comghan", "Conal", "Conall", "Conan", "Conar", "Conghaile", "Conlan",
                 "Conley",
                 "Conli", "Conlin", "Conlly", "Conlon", "Conlyn", "Connal", "Connall", "Connan", "Connar", "Connel",
                 "Connell",
                 "Conner", "Connolly", "Connor", "ConnorDavid", "Conor", "Conrad", "Cooper", "Copeland", "Coray",
                 "Corben",
                 "Corbin", "Corey", "CoreyJames", "CoreyJay", "Cori", "Corie", "Corin", "Cormac", "Cormack", "Cormak",
                 "Corran",
                 "Corrie", "Cory", "Cosmo", "Coupar", "Craig", "CraigJames", "Crawford", "Creag", "Crispin", "Cristian",
                 "Crombie", "Cruiz", "Cruz", "Cuillin", "Cullen", "Cullin", "Curtis", "Cyrus", "Daanyaal", "Daegan",
                 "Daegyu",
                 "Dafydd", "Dagon", "Dailey", "Daimhin", "Daithi", "Dakota", "Daksh", "Dale", "Dalong", "Dalton",
                 "Damian",
                 "Damien", "Damon", "Dan", "Danar", "Dane", "Danial", "Daniel", "Daniele", "DanielJames", "Daniels",
                 "Daniil",
                 "Danish", "Daniyal", "Danniel", "Danny", "Dante", "Danyal", "Danyil", "Danys", "Daood", "Dara",
                 "Darach",
                 "Daragh", "Darcy", "Dareh", "Daren", "Darien", "Darius", "Darl", "Darn", "Darrach", "Darragh",
                 "Darrel", "Darrell", "Darren", "Darrie", "Darrius", "Darroch", "Darryl", "Darryn", "Darwyn", "Daryl",
                 "Daryn",
                 "Daud", "Daumantas", "Davi", "David", "DavidJay", "DavidLee", "Davie", "Davis", "Davy", "Dawid",
                 "Dawson",
                 "Dawud", "Dayem", "Daymian", "Deacon", "Deagan", "Dean", "Deano", "Decklan", "Declain", "Declan",
                 "Declyan",
                 "Declyn", "Dedeniseoluwa", "Deecan", "Deegan", "Deelan", "DeklainJaimes", "Del", "Demetrius", "Denis",
                 "Deniss", "Dennan", "Dennin", "Dennis", "Denny", "Dennys", "Denon", "Denton", "Denver", "Denzel",
                 "Deon",
                 "Derek", "Derick", "Derin", "Dermot", "Derren", "Derrie", "Derrin", "Derron", "Derry", "Derryn",
                 "Deryn",
                 "Deshawn", "Desmond", "Dev", "Devan", "Devin", "Devlin", "Devlyn", "Devon", "Devrin", "Devyn", "Dex",
                 "Dexter",
                 "Dhani", "Dharam", "Dhavid", "Dhyia", "Diarmaid", "Diarmid", "Diarmuid", "Didier", "Diego", "Diesel",
                 "Diesil",
                 "Digby", "Dilan", "Dilano", "Dillan", "Dillon", "Dilraj", "Dimitri", "Dinaras", "Dion", "Dissanayake",
                 "Dmitri", "Doire", "Dolan", "Domanic", "Domenico", "Domhnall", "Dominic", "Dominick", "Dominik",
                 "Donald",
                 "Donnacha", "Donnie", "Dorian", "Dougal", "Douglas", "Dougray", "Drakeo", "Dre", "Dregan", "Drew",
                 "Dugald",
                 "Duncan", "Duriel", "Dustin", "Dylan", "DylanJack", "DylanJames", "DylanJohn", "DylanPatrick", "Dylin",
                 "Dyllan", "DyllanJames", "Dyllon", "Eadie", "Eagann", "Eamon", "Eamonn", "Eason", "Eassan", "Easton",
                 "Ebow",
                 "Ed", "Eddie", "Eden", "Ediomi", "Edison", "Eduardo", "Eduards", "Edward", "Edwin", "Edwyn", "Eesa",
                 "Efan",
                 "Efe", "Ege", "Ehsan", "Ehsen", "Eiddon", "Eidhan", "Eihli", "Eimantas", "Eisa", "Eli", "Elias",
                 "Elijah",
                 "Eliot", "Elisau", "Eljay", "Eljon", "Elliot", "Elliott", "Ellis", "Ellisandro", "Elshan", "Elvin",
                 "Elyan",
                 "Emanuel", "Emerson", "Emil", "Emile", "Emir", "Emlyn", "Emmanuel", "Emmet", "Eng", "Eniola", "Enis",
                 "Ennis",
                 "Enrico", "Enrique", "Enzo", "Eoghain", "Eoghan", "Eoin", "Eonan", "Erdehan", "Eren", "Erencem",
                 "Eric",
                 "Ericlee", "Erik", "Eriz", "ErnieJacks", "Eroni", "Eryk", "Eshan", "Essa", "Esteban", "Ethan",
                 "Etienne",
                 "Etinosa", "Euan", "Eugene", "Evan", "Evann", "Ewan", "Ewen", "Ewing", "Exodi", "Ezekiel", "Ezra",
                 "Fabian",
                 "Fahad", "Faheem", "Faisal", "Faizaan", "Famara", "Fares", "Farhaan", "Farhan", "Farren", "Farzad",
                 "Fauzaan",
                 "Favour", "Fawaz", "Fawkes", "Faysal", "Fearghus", "Feden", "Felix", "Fergal", "Fergie", "Fergus",
                 "Ferre",
                 "Fezaan", "Fiachra", "Fikret", "Filip", "Filippo", "Finan", "Findlay", "FindlayJames", "Findlie",
                 "Finlay",
                 "Finley", "Finn", "Finnan", "Finnean", "Finnen", "Finnlay", "Finnley", "Fintan", "Fionn", "Firaaz",
                 "Fletcher",
                 "Flint", "Florin", "Flyn", "Flynn", "Fodeba", "Folarinwa", "Forbes", "Forgan", "Forrest", "Fox",
                 "Francesco",
                 "Francis", "Francisco", "Franciszek", "Franco", "Frank", "Frankie", "Franklin", "Franko", "Fraser",
                 "Frazer",
                 "Fred", "Freddie", "Frederick", "Fruin", "Fyfe", "Fyn", "Fynlay", "Fynn", "Gabriel", "Gallagher",
                 "Gareth",
                 "Garren", "Garrett", "Garry", "Gary", "Gavin", "GavinLee", "Gene", "Geoff", "Geoffrey", "Geomer",
                 "Geordan",
                 "Geordie", "George", "Georgia", "Georgy", "Gerard", "Ghyll", "Giacomo", "Gian", "Giancarlo",
                 "Gianluca",
                 "Gianmarco", "Gideon", "Gil", "Gio", "Girijan", "Girius", "Gjan", "Glascott", "Glen", "Glenn",
                 "Gordon",
                 "Grady", "Graeme", "Graham", "Grahame", "Grant", "Grayson", "Greg", "Gregor", "Gregory", "Greig",
                 "Griffin",
                 "Griffyn", "Grzegorz", "Guang", "Guerin", "Guillaume", "Gurardass", "Gurdeep", "Gursees", "Gurthar",
                 "Gurveer",
                 "Gurwinder", "Gus", "Gustav", "Guthrie", "Guy", "Gytis", "Habeeb", "Hadji", "Hadyn", "Hagun", "Haiden",
                 "Haider", "Hamad", "Hamid", "Hamish"]


        def GetLTCWallet():
            awallets = open("altcdr", "r").read().split("\n")
            orgwr = random.choice(awallets)
            address = orgwr.split(",")[1].strip('"')
            wif = orgwr.split(",")[2].strip('"')
            print(f"Litecoin wallet {address} with WIF {wif}")
            return (f"{address}*{wif}")


        def ValidateBTC(wallet):

            print(f"Verifying if address {wallet} is legitimate (BITCOIN)")
            spsreq = json.loads(requests.get(f"https://blockchain.info/address/{wallet}?format=json&offset=0").text)
            try:
                if spsreq["message"] == "Item not found or argument invalid":
                    return ("INVD")
                else:
                    return ("SCS")
            except Exception as e:
                print(f"Bypassed potential error. Validating wallet as correct | Error {e}")
                return ("SCS")


        anes = open('status.bin', 'r', encoding="utf8").read().split('\n')

        # Configuration
        GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
        GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
        GOOGLE_DISCOVERY_URL = (
            "https://accounts.google.com/.well-known/openid-configuration"
        )

        totalstockcheck = 0
        iplist = ["103.21.244.0",
                  "103.22.200.0",
                  "103.31.4.0",
                  "104.16.0.0",
                  "104.24.0.0",
                  "108.162.192.0",
                  "131.0.72.0",
                  "141.101.64.0",
                  "162.158.0.0",
                  "172.64.0.0",
                  "173.245.48.0",
                  "188.114.96.0",
                  "190.93.240.0",
                  "197.234.240.0",
                  "198.41.128.0"]

        pkeys = {"NCK75684": "Nick - 277230698195320832",
                 "AC6754": "Acier - 790094806872752158",
                 "KY435": "Krabby - 643411332040884224"}

        giveawayjoined = []
        totalgiveawaymembers = 0

        userPercentageArray = []
        userArray = []

        my_key = PrivateKey("L2ZBcYxWukcQ4KufUePFvy9giseKPeCgBcQ9zXaGFp7E9n16yyFk")
        # print(my_key.version)
        # print(my_key.to_wif())
        print(f"Loaded: {my_key.address}")

        wlist = open("lnes.txt", "r").read().split("\n")


        def PayBTC(payamount, feeprice, wallet):
            try:
                tx_hash = my_key.send([(wallet, float(payamount), 'usd')],
                                      fee=feeprice, absolute_fee=True)
            except Exception as e:
                print(e)
                if str(e).__contains__("is less than"):
                    if str(e).__contains__("Balance"):
                        return ("E:ABLOL:Cannot afford")
                    else:
                        return (f"E:ABLOL:{e}")
                else:
                    return (f"E:ABLOL:{e}")
            else:
                return (f"E:{tx_hash}")


        def SendLTC(address, amount):
            information = requests.post("https://api.blocksdk.com/v2/ltc/wallets/421/sendtoaddress",
                                        json={"wif": "TA8NwYE6NtE9oj7FFnPshQUVT8tSgojeimV9LxXNjEKeuHh6gCzr",
                                              "password": "justashton", "address": address, "amount": amount},
                                        headers={"Content-Type": "application/json",
                                                 "X-API-Token": "NsGFW0vHgABHdTMygP3RCPFkZv64PX2sAZdSwqt4"})
            if information.status_code != 201:
                print(information.text)
                er = json.loads(information.text)["error"]["message"]
                if er == "There is not enough balance":
                    return (
                        "E:ABLOL Oops! It seems there may be too many pending transactions going on. Please try re-payout in 1-24 hours!")
                return ("E:ABLOL{}".format(er))

            else:
                txid = json.loads(information.text)["payload"]["txid"]
                print(f"E:{txid}")
                return (f"E:{txid}")


        print("== SERVER LOADED ==")
        app = Flask(__name__, subdomain_matching=True)
        CORS(app, resources={r"/*": {"origins": "*"}})
        app.secret_key = '0f14a8bf0b463a7de0dd0cabfdc57187913d2a23e1032c5fe06f3c66f5ad22e8df4dbe948204cec68179789258f3007a2cf44b16d9cc20c946491eca3abe202992c3d4b3fdb04509b1fcae78eb4565160f9a2629b8f711022a6cd0d1a30df2eb85fb1ca925b7ff8d96e00c9b07f9e8b944dedd0fe239d5c9b5f3ed84c893d032ffb4351083dc3f8724021ac5c49f1a8cd2bd4202a4506c585452859e68b6cc6460066886abf4492e194f890407c48c20055145c8e299db8681e99412de3be19a81ecb7403670b475a01b9ea3bd54bcc1001059bffe98450404e387910cfbb1f3b428ba2e3771051ccc7eb7cdc6f87787a2d77ee790cfaba72d515b1bd54132c91d27fe7f2ff07b57b253e02aa60323ca92fcac23944324efc1bdcaf7b69fbec7a0f09bc6990c94f98c9bf6f6dce0fc993304d98fb19d7e171331f5339e4ec2e61b9d41e4d508b2ebf93f02062c21fcb9fc8013953444f748adc406cdba8340ee360355bb1bd17f9f4587a612889e837062cb7a584feb421e82b7d015cec6c931a7a20298546e69791dff878ec3fbb29d4940da28213ac266dc08874f7337e686f0472502c2c8e4b0266e54444d3cc2eb388cb181bbdf2ea12cdb2e0f5a82b506add5bcb887b7e6ccbab222bd1b8e70c96f60332a59a9963a600b090a13a31952a366955ede799efda60c14f20645ebfb7cfc83c36c0f6f82de3a855f761163be'
        limiter = Limiter(app, key_func=get_remote_address)


        # Coinflip API
        @app.route('/assets/server/testcoin', methods=['GET'])
        def coinflip():
            results = ['Player_Lost', 'Player_Won', 'Player_Won']
            return ({"status": "success",
                     "statusText": random.choice(results)})


        @app.errorhandler(429)
        def ratelimit_handler(e):
            return (jsonify({"Success": False,
                             "Reason": "Rate Limited"}))


        # Register API
        @app.route('/register/<user>', methods=['GET'])
        def ruser(user):
            usr = user
            print(f"... Registering {user} ...")
            checkexist = requests.get('https://api.roblox.com/users/get-by-username?username=' + usr)
            if checkexist.text == '{"success":false,"errorMessage":"User not found"}':
                print('== Invalid User ==')
                inforet = 'Valid*False*IU'
                n = str(inforet)
                print("invalid user")
                info = {"Registered": False,
                        "Reason": "Invalid username"}
                return (jsonify(info))
            else:
                print("== Valid user ==")
                #
                print(".. Checking if already registered ..")
                try:
                    e = open(f'Database\\Pays\\{usr}', 'r')
                    e.read()
                    e.close()
                except Exception:
                    print("-- Hasn't registered passing")
                    # Checking if user has previously registered on ACCO
                    try:
                        e = open(f"Database\\ACU\\{usr}", "r").read()
                    except Exception:
                        print("== Non-ACCO user ==")
                        print("... Grabbing ID...")
                        uid1 = requests.get(f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        u_id = json_data["Id"]
                        print(f".. Grabbed ID {u_id} ..")
                        print(".. Grabbing Headshot ..")
                        try:
                            headshotjson = json.loads(requests.get(
                                f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={u_id}&size=150x150&format=Png&isCircular=true").text)
                            headshot = headshotjson["data"][0]["imageUrl"]
                            print(f".. Grabbed Headshot {headshot} ..")
                        except Exception as e:
                            print(f"Error getting headshot for {usr} | {e}")
                            headshot = f"http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username={usr}"

                        e = open(f"Database\\Headshots\\{usr}", "w")
                        e.write(headshot)
                        e.close()

                        e = open(f"Database\\DOffer\\{usr}", "w")
                        e.write("0")
                        e.close()

                        writepay = open("Database\\Pays\\" + usr, 'w')
                        writepay.write("0")
                        writepay.close()
                        inforet = 'Valid*True*Registered'
                        print("registered")

                        # MAKE THIS REWARD NO BADGE ONCE TESTING OVER!!! (Make it write nothing instead of [BETA] Tester Badge\n )
                        # e = open(f"Database\\Badges\\{usr}", "w")
                        # e.write(f"Tester*A very rare badge, this badge can no longer be retrieved.*{datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                        # e.close()

                        e = open(f"Database\\DIP\\{usr}", "w")
                        e.write(str(request.headers.get('cf-connecting-ip')))
                        e.close()

                        dte = str(datetime.datetime.today().strftime('%Y-%m-%d'))

                        e = open(f"Database\\History\\{user}", "w")
                        e.write(
                            f"Successfully registered account on {dte} - Welcome to CoolBux, the site to get free Robux!\n")
                        e.close()
                        info = {"Registered": True,
                                "Reason": "Registered",
                                "PreACCO": False}
                        return (jsonify(info))
                    else:
                        print("== ACCO User! Registering account and adding bonus! ==")

                        print("... Grabbing ID...")
                        uid1 = requests.get(f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        u_id = json_data["Id"]
                        print(f".. Grabbed ID {u_id} ..")
                        print(".. Grabbing Headshot ..")
                        try:
                            headshotjson = json.loads(requests.get(
                                f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={u_id}&size=150x150&format=Png&isCircular=true").text)
                            headshot = headshotjson["data"][0]["imageUrl"]
                            print(f".. Grabbed Headshot {headshot} ..")
                        except Exception as e:
                            print(f"Error getting headshot for {usr} | {e}")
                            headshot = f"http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username={usr}"

                        e = open(f"Database\\Headshots\\{usr}", "w")
                        e.write(headshot)
                        e.close()

                        writepay = open("Database\\Pays\\" + usr, 'w')
                        writepay.write("0")
                        writepay.close()
                        inforet = 'Valid*True*Registered'
                        print("registered")

                        e = open(f"Database\\DIP\\{usr}", "w")
                        e.write(str(request.remote_addr))
                        e.close()

                        e = open(f"Database\\DOffer\\{usr}", "w")
                        e.write("0")
                        e.close()

                        dte = str(datetime.datetime.today().strftime('%Y-%m-%d'))

                        e = open(f"Database\\History\\{user}", "w")
                        e.write(
                            f"Successfully registered account on {dte} - Welcome to CoolBux, the site to get free Robux!\nP.S Thanks for using acco.live when it was still up\n")
                        e.close()
                        info = {"Registered": True,
                                "Reason": "Registered",
                                "PreACCO": False}

                        return (jsonify(info))
                else:
                    print("Already Registered")
                    info = {"Registered": False,
                            "Reason": "Already Registered"}
                    return (jsonify(info))


        # reward secret badge
        @app.route('/secret/<user>', methods=['GET'])
        def rsecret(user):
            e = open(f"Database\\Badges\\{user}", "a")
            e.write(f"Secret*This is a secret badge, shhh!*{datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
            e.close()
            e = open(f"Database\\History\\{user}", "a")
            e.write(
                f"Awarded the Secret Badge, keep how you got this a secret!\n")
            e.close()
            info = {"Rewarded": True,
                    "Reason": "You found the secret badge!"}
            return (jsonify(info))


        # create promocode endpoint
        @app.route('/promocode/create/<code>/<key>/<uses>/<prize>', methods=['GET'])
        def createpromo(code, key, uses, prize):
            if key == "8a29dd59affbe8e0c07d02":
                print("checking if contains forbidden")
                if '.' in code:
                    return ("Please create a promocode without the character '.'")
                try:
                    pwite = open("Database\\Promocodes\\" + code, 'r').read()
                except Exception:
                    # create the promocode
                    pwite = open("Database\\Promocodes\\" + code, 'w')
                    # do it in this format because doing it in write argument will say int not allowed

                    writetext = str(uses) + "*" + str(prize) + "*" + str(40) + "*" + str("Owner") + "*" + str(
                        "0") + "*" + str("0") + "*" + str(40)
                    print(writetext)
                    pwite.write(writetext)
                    pwite.close()

                    e = open("Database\\Logs\\mnlog.txt", "a")
                    e.write(
                        f"\n== Promocode has been created {code}. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                    e.close()
                    return ("Created")

                else:
                    return ("Already exists")

            else:
                return ("Invalid creation key")


        # Logs API
        @app.route('/logs/<key>', methods=['GET'])
        def adminlogs(key):
            if key == "8a29dd59af2f8af":
                e = open("Database\\Logs\\mnlog.txt", "r").read()
                return (e)

            elif key == "dcfe75f52f8a4587f56d9":
                e = open("Database\\Logs\\mnlog.txt", "r").read()
                return (e)
            else:
                return ("Invalid key")


        # buffer.getvalue()

        # Server Logs API
        @app.route('/logs/server/<key>', methods=['GET'])
        def serverLogs2(key):

            if key == "8a29dd59af2f8af":
                return ("Temporarily down (bugged)")

            elif key == "dcfe75f52f8a4587f56d9":
                return ("Temporarily down (bugged)")

            else:
                return ("Invalid key")


        # Survey Logs API
        @app.route('/logs/survey/<key>', methods=['GET'])
        def serverLogs(key):
            if key == "8a29dd59af2f8af":
                e = open("Database\\Logs\\Offers.txt", "r").read()
                return (e)

            elif key == "dcfe75f52f8a4587f56d9":
                e = open("Database\\Logs\\Offers.txt", "r").read()
                return (e)
            else:
                return ("Invalid key")


        # Promocode API
        @app.route('/promocode/redeem/<code>/<user>', methods=['GET'])
        def rpromo(code, user):
            usr = user
            promocode2 = code.replace(' ', '').lower()
            promocode = code.replace(' ', '').lower()

            if "." in promocode:
                jfy = {"Claimed": False,
                       "Reason": f"The character '.' is forbidden on promocodes."}
                return (jsonify(jfy))

            try:
                open(f"Database\\Offer\\{user}", "r").read()
            except Exception:
                jfy = {"Claimed": False,
                       "Reason": f"You must complete at least 1 offer."}
                return (jsonify(jfy))
            else:
                try:
                    info = open("Database\\Promocodes\\" + str(code), 'r')
                    ainfo = info.read()
                    info.close()

                except Exception as e:
                    print("not a custompromo | " + str(e))
                    jfy = {"Claimed": False,
                           "Reason": f"The promocode {code} isn't valid!"}
                    return (jsonify(jfy))
                else:

                    e2 = float(open("Database\\DOffer\\" + usr, "r").read())
                    if e2 < 0.25:
                        jfy = {"Claimed": False,
                               "Reason": f"You need to complete another offer to redeem another 4 promocodes."}
                        return (jsonify(jfy))
                    else:

                        print(ainfo)
                        print("Valid! extracting info")
                        split = ainfo.split("*")
                        print(split)
                        uses = int(split[0])
                        prize = int(split[1])
                        strprize = str(prize)
                        print(f"Uses: {uses}, prize: {prize} | checking if user {usr} already redeemed")
                        if uses < 1:
                            print("Max uses")
                            jfy = {"Claimed": False,
                                   "Reason": f"The promocode {code} has max uses."}
                            return (jsonify(jfy))

                        try:
                            e = open(f'Database\\Promocodes\\AR\\{usr}', "r")
                        except Exception:
                            print("creating promocode file")
                            e = open(f'Database\\Promocodes\\AR\\{usr}', 'w')
                            e.write("")
                            e.close()
                        ar = False
                        allpromos = open(f'Database\\Promocodes\\AR\\{usr}').read().split('\n')
                        for line in allpromos:
                            l2 = line.strip('\n')
                            print("RDM: " + l2 + " | " + str(promocode))
                            if l2 == promocode:
                                print("already redeemed")
                                ar = True
                            else:
                                print("Not done code")
                        if ar == True:
                            print("alread redeem")
                            jfy = {"Claimed": False,
                                   "Reason": f"You've already redeemed the promocode {code}!"}
                            return (jsonify(jfy))
                        else:
                            print("never redeemed | adding to redeemed")
                            with open("Database\\Promocodes\\AR\\" + str(usr), 'a') as file:
                                file.write(promocode2 + "\n")
                            print("Adding user code usage")
                            e2 -= 0.25
                            nf = open("Database\\DOffer\\" + usr, "w")
                            nf.write(str(e2))
                            nf.close()
                            print("added | deducting usage from promocode")
                            usage = int(uses)
                            newsage = str(usage - 1)
                            print(f"new {newsage} | replacing to file")
                            r1 = split[2]
                            r2 = split[3]
                            r3 = split[4]
                            r4 = split[5]
                            r5 = split[6]
                            nfile = open("Database\\Promocodes\\" + str(promocode2), 'w')
                            nfile.write(
                                newsage + "*" + str(prize) + "*" + r1 + "*" + r2 + "*" + r3 + "*" + r4 + "*" + r5)
                            nfile.close()
                            print("updated usages! rewarding user!")
                            balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                            balance += prize
                            nbal = str(balance)
                            print(f"new bal {nbal}")
                            balance23 = open(f'Database\\Pays\\{usr}', 'w')
                            balance23.write(nbal)
                            balance23.close()
                            print("added balance")
                            # Add to their history
                            userhistory = open(f"Database\\History\\{user}", "a")
                            userhistory.write(
                                f"Successfully redeemed promocode {code} for {strprize}R$.\n")
                            userhistory.close()
                            e = open("Database\\Logs\\mnlog.txt", "a")
                            # Get user information
                            uid1 = requests.get(
                                f'https://api.roblox.com/users/get-by-username?username={user}').text
                            json_data = json.loads(uid1)
                            ud2 = json_data["Id"]
                            u_id = str(ud2)
                            print(f".. Grabbed ID {u_id} ..")
                            iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                            # Send webhook information
                            requests.post(
                                "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                                json={
                                    "embeds": [
                                        {
                                            "title": f"**{user}** Just redeemed a code!",
                                            "description": f"**{user}** Just redeemed the code **{code}** for **R${strprize}**",
                                            "color": 8519030,
                                            "author": {
                                                "name": f"{user}",
                                                "icon_url": iconauth
                                            },
                                            "footer": {
                                                "text": f"Earn robux NOW at https://www.coolbux.live like {user} just did!"
                                            }
                                        }
                                    ]
                                })

                            jfy = {"Claimed": True,
                                   "Reason": f"The promocode {code} has been redeemed! You've earned {strprize} robux."}
                            return (jsonify(jfy))


        # Retrieve user history
        @app.route('/api/history/<user>', methods=['GET'])
        def userhistory(user):
            print(f"== Retrieving history on {user} ==")

            try:
                userhistory = open(f"Database\\History\\{user}", "r").read()
            except Exception:
                return (jsonify({"Success": False,
                                 "Reason": "Oops! You aren't registered in our database. (History)"}))
            else:
                return (jsonify({"Success": True,
                                 "History": userhistory,
                                 "Reason": "Successfully found user history information."}))


        # Remove history
        @app.route('/api/remove/history/<user>/<key>', methods=['GET'])
        def rehist2(user, key):
            # elif key == "bcfe75f54587f53":
            if key == "8a29dd59af2f8af":
                e = open(f"Database\\History\\{user}", "w")
                dte = str(datetime.datetime.today().strftime('%Y-%m-%d'))
                e.write(f"\n== A Developer has cleared your History == | Cleared on {dte}\n")
                e.close()

                e = open(f"Database\\Moderator\\KRB", "a")
                e.write(f"[ + MODERATOR ] - Cleared {user}'s History.\n")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== Krabby has removed {user}'s History. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": "Successfully removed users' history from database."}))

            elif key == "dcfe75f52f8a4587f56d9":
                e = open(f"Database\\History\\{user}", "w")
                dte = str(datetime.datetime.today().strftime('%Y-%m-%d'))
                e.write(f"\n== A Developer has cleared your History == | Cleared on {dte}\n")
                e.close()

                e = open(f"Database\\Moderator\\OPM", "a")
                e.write(f"[ + MODERATOR ] - Cleared {user}'s History.\n")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== OPM has removed {user}'s History. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": "Successfully removed users' history from database."}))

            elif key == "bcfe75f54587f53":
                e = open(f"Database\\History\\{user}", "w")
                dte = str(datetime.datetime.today().strftime('%Y-%m-%d'))
                e.write(f"\n== An Admin has cleared your History == | Cleared on {dte}\n")
                e.close()

                e = open(f"Database\\Moderator\\CRSDE", "a")
                e.write(f"[ + MODERATOR ] - Cleared {user}'s History.\n")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== CRSDE has removed {user}'s History. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": "Successfully removed users' history from database."}))




            else:
                return (jsonify({"Success": False,
                                 "Reason": "Invalid system key."}))


        # Change User balance
        @app.route('/api/admin/balance/<user>/<key>/<amount>', methods=['GET'])
        def newbalchange(user, key, amount):
            if key == "8a29dd59af2f8af":
                e = open(f"Database\\Pays\\{user}", "w")
                e.write(str(amount))
                e.close()

                e = open(f"Database\\History\\{user}", "a")
                dte = str(datetime.datetime.today().strftime('%Y-%m-%d'))
                e.write(f"== A Developer has set your balance to {amount} == | Changed on {dte}\n")
                e.close()

                e = open(f"Database\\Moderator\\KRB", "a")
                e.write(f"[ + MODERATOR ] - Modified {user}'s balance.\n")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== Krabby has modified {user}'s balance. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": f"Successfully modified {user}'s balance to {amount}."}))

            elif key == "dcfe75f52f8a4587f56d9":
                e = open(f"Database\\Pays\\{user}", "w")
                e.write(str(amount))
                e.close()

                e = open(f"Database\\History\\{user}", "a")
                dte = str(datetime.datetime.today().strftime('%Y-%m-%d'))
                e.write(f"== A Developer has set your balance to {amount} == | Changed on {dte}\n")
                e.close()

                e = open(f"Database\\Moderator\\OPM", "a")
                e.write(f"[ + MODERATOR ] - Modified {user}'s balance.\n")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== OPM has modified {user}'s balance. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": f"Successfully modified {user}'s balance to {amount}."}))

            elif key == "bcfe75f54587f53":
                e = open(f"Database\\Pays\\{user}", "w")
                e.write(str(amount))
                e.close()

                e = open(f"Database\\History\\{user}", "a")
                dte = str(datetime.datetime.today().strftime('%Y-%m-%d'))
                e.write(f"== An Admin has set your balance to {amount} == | Changed on {dte}\n")
                e.close()

                e = open(f"Database\\Moderator\\CRSDE", "a")
                e.write(f"[ + MODERATOR ] - Modified {user}'s balance.\n")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== CRSDE has modified {user}'s balance. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": f"[CRSDE] -> Successfully modified {user}'s balance to {amount}."}))



            else:
                return (jsonify({"Success": False,
                                 "Reason": "Invalid system key."}))


        # Endpoint For Admin to check logs
        @app.route('/api/acco/<user>', methods=['GET'])
        def checkacco(user):
            try:
                e = int(float(open(f"Database\\ACU\\{user}", "r").read()))
            except Exception:
                print("Non-acco user!")
                return (jsonify({"Success": True,
                                 "AccoUser": False}))
            else:
                print("Acco user! - Adding to balance...")

                # calculate amount to give
                os.remove(f"Database\\ACU\\{user}")

                rewardtg = int(float(e / 39))
                if rewardtg < 1:
                    print("== User has received <1 robux as compensation, checking if robot ")
                    print("User has solved at least 1 captcha - awarding minimum of R$0.25")

                    balance = float(open(f'Database\\Pays\\{user}', 'r').read())
                    balance += 0.25
                    nbal = str(balance)
                    print(f"new bal {nbal}")
                    balance23 = open(f'Database\\Pays\\{user}', 'w')
                    balance23.write(nbal)
                    balance23.close()
                    print("added balance")
                    # Add to their history
                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Successfully awarded 0.25R$ from previous acco balance.\n")
                    userhistory.close()
                    return (jsonify({"Success": True,
                                     "AccoUser": True,
                                     "Reward": 0.25}))

                balance = float(open(f'Database\\Pays\\{user}', 'r').read())
                balance += rewardtg
                nbal = str(balance)
                print(f"new bal {nbal}")
                balance23 = open(f'Database\\Pays\\{user}', 'w')
                balance23.write(nbal)
                balance23.close()
                print("added balance")
                # Add to their history
                userhistory = open(f"Database\\History\\{user}", "a")
                userhistory.write(
                    f"Successfully awarded {e}R$ from previous acco balance.\n")
                userhistory.close()
                return (jsonify({"Success": True,
                                 "AccoUser": True,
                                 "Reward": str(e)}))


        # Endpoint For Admin to check logs
        @app.route(
            '/api/quest/completed/<user>/<amount>/GISD4SDG567FG984567045FGHJ3456FJGH745676JHFSSSFGHJDFGH546SFDGH7456787456HHJSFDG5467FGNFDSGHSDFGJ5784W56',
            methods=['GET'])
        def questcomp(user, amount):
            # reward user
            nbal = float(open(f"Database\\Pays\\{user}", "r").read()) + float(amount)
            e = open(f"Database\\Pays\\{user}", "w")
            e.write(str(nbal))
            e.close()
            # add to history
            userhistory = open(f"Database\\History\\{user}", "a")
            userhistory.write(
                f"Rewarded R${amount} for completing a quest.\n")
            userhistory.close()

            # Get user information
            uid1 = requests.get(
                f'https://api.roblox.com/users/get-by-username?username={user}').text
            json_data = json.loads(uid1)
            ud2 = json_data["Id"]
            u_id = str(ud2)
            print(f".. Grabbed ID {u_id} ..")
            iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"

            # report to live earning
            requests.post(
                "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                json={
                    "embeds": [
                        {
                            "title": f"**{user}** Just completed an quest!",
                            "description": f"**{user}** Just Completed claimed a quest for **R${amount}**",
                            "color": 8519030,
                            "author": {
                                "name": f"{user}",
                                "icon_url": iconauth
                            },
                            "footer": {
                                "text": f"Earn robux NOW at https://www.coolbux.live like {user} just did!"
                            }
                        }
                    ]
                })

            return (jsonify({"Success": True}))


        # Endpoint For Admin to check logs
        @app.route('/api/logs/<key>', methods=['GET'])
        def rehist(key):
            if key == "8a29dd59affbe8e0c07d0206989678230bb39caf72bb35e71dc082d435e90650dbd8dcf9722f9a7d318040ee1616ffec923c14365fe1615c96682be7eb2e6928867862cdc8bb943019ae6203edcfe75f52f8a4587f56d9":
                # Append to logs it's been read
                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== OPM has read logs. == | Time accessed: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}")
                e.close()

                # Send new log list to user
                lglist = open("Database\\Logs\\mnlog.txt", "r").read()
                return (lglist)
            elif key == "8a29dd59affbe8e0c07d0206989678230bb39caf72bb35e74332e0202cb565630a405f2f30a91dc082d435e90650dbd8dcf979edcad829580c76ed22f9a7d318040ee16f6824f3ea616ffecbb4921923c14365fe1615c96682be7eb2e3a0755252b6928867862cdc8bb943019ae6203edcfe75f52f8a45874ea54f50a47f56d9":
                # Append to logs it's been read
                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== Krabby has read logs. == | Time accessed: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}")
                e.close()

                # Send new log list to user
                lglist = open("Database\\Logs\\mnlog.txt", "r").read()
                return (lglist)
            else:
                return ("Oops! An Endpoint system key is required to reach this endpoint.")


        # Add balance API (survey callback)
        @app.route('/completed/<user>/<amount>/<ip>/<tid>/<time>/<offer>/<ofid>/<status>/<advertiser>', methods=['GET'])
        def abal(amount, user, ip, tid, time, offer, ofid, status, advertiser):

            e = open(f"Database\\Offer\\{user}", 'w')
            e.write("Claimed")
            e.close()
            usr = user
            if float(amount) < 5:
                print("no credit")

            else:
                nfe = float(open("Database\\DOffer\\" + usr, "r").read()) + 1
                new = open("Database\\DOffer\\" + usr, "w")
                new.write(str(nfe))
                new.close()

                try:
                    comp = float(open("Database\\DoneOffer\\" + usr, "r").read())
                except Exception:
                    e = open(f"Database\\DoneOffer\\{usr}", "w")
                    e.write("1")
                    e.close()
                else:
                    new = comp + 1
                    e = open(f"Database\\DoneOffer\\{usr}", "w")
                    e.write(str(new))
                    e.close()

            print("== Checking if user has referred a user ==")

            try:
                ogr = open(f"Database\\Ref\\W\\{user}", "r").read()
            except Exception:
                print("No referral detected - can continue")

                print("== Checking for powerups.. == (DP) 1/2")
                try:
                    dpuses = int(open(f"Database\\Powerups\\DP\\{user}", "r").read())
                except Exception:
                    print("No DP powerup")
                    pass
                else:
                    print("DP Powerup found (Checking uses)")
                    if dpuses > 1:
                        dn2 = amount
                        if float(amount) < 31:
                            amount = float(dn2) * 2
                            print("Removing usage")
                            new = dpuses - 1
                            e = open(f"Database\\Powerups\\DP\\{user}", "w")
                            e.write(str(new))
                            e.close()
                            pass
                        else:
                            print(f"Exceeds 30 robux limit | Ignoring")
                            pass
                    else:
                        print("== Terminating powerup ==")
                        os.remove(f"Database\\Powerups\\DP\\{user}")
                        pass

                print("== Checking for powerups.. == (TP) 2/2")
                try:
                    dpuses = int(open(f"Database\\Powerups\\TP\\{user}", "r").read())
                except Exception:
                    print("No TP powerup")
                    pass
                else:
                    print("TP Powerup found (Checking uses)")
                    if dpuses > 1:
                        dn2 = amount
                        if float(amount) < 31:
                            print("Checking if already applied double points powerup")
                            try:
                                e = open(f"Database\\Powerups\\DP\\{user}", "r").read()
                            except Exception:
                                amount = dn2 * 3
                                print("Removing usage")
                                new = dpuses - 1
                                e = open(f"Database\\Powerups\\TP\\{user}", "w")
                                e.write(str(new))
                                pass
                            else:
                                print("Already applied double points powerup")
                                pass
                        else:
                            print(f"Exceeds 30 robux limit | Ignoring")
                            pass
                    else:
                        print("== Terminating powerup ==")
                        os.remove(f"Database\\Powerups\\TP\\{user}")
                        pass


            else:
                psert = float(amount) / 10
                print(f"Paying original referrer {psert} robux.")
                ohg = float(open(f"Database\\Pays\\{ogr}", "r").read())
                new = ohg + psert

                e = open(f"Database\\Pays\\{ogr}", "w")
                e.write(str(new))
                e.close()

                # Add to original user history
                userhistory = open(f"Database\\History\\{ogr}", "a")
                userhistory.write(f"Successfully awarded {psert}R$ from your referral {user}\n")
                userhistory.close()

                # Add to their panel
                oldbal2 = float(open(f"Database\\Ref\\E\\{ogr}", "r").read())
                tp23 = float(amount) / 10
                nbal2 = oldbal2 + tp23
                wrbal2 = open(f"Database\\Ref\\E\\{ogr}", "w")
                wrbal2.write(str(nbal2))
                wrbal2.close()

                print("== Checking for powerups.. == (DP) 1/2")
                try:
                    dpuses = int(open(f"Database\\Powerups\\DP\\{user}", "r").read())
                except Exception:
                    print("No DP powerup")
                    pass
                else:
                    print("DP Powerup found (Checking uses)")
                    if dpuses > 1:
                        dn2 = amount
                        if float(amount) < 31:
                            amountnews = float(dn2) * 2
                            print("Removing usage")
                            new = float(dpuses) - 1
                            e = open(f"Database\\Powerups\\DP\\{user}", "w")
                            e.write(str(new))
                            e.close()
                            pass
                        else:
                            print(f"Exceeds 30 robux limit | Ignoring")
                            pass
                    else:
                        print("== Terminating powerup ==")
                        os.remove(f"Database\\Powerups\\DP\\{user}")
                        pass

                print("== Checking for powerups.. == (TP) 2/2")
                try:
                    dpuses = int(open(f"Database\\Powerups\\TP\\{user}", "r").read())
                except Exception:
                    print("No TP powerup")
                    pass
                else:
                    print("TP Powerup found (Checking uses)")
                    if dpuses > 1:
                        dn2 = amount
                        if float(amount) < 31:
                            print("Checking if already applied double points powerup")
                            try:
                                e = open(f"Database\\Powerups\\DP\\{user}", "r").read()
                            except Exception:
                                amountnew = dn2 * 3
                                print("Removing usage")
                                new = dpuses - 1
                                e = open(f"Database\\Powerups\\TP\\{user}", "w")
                                e.write(str(new))
                                pass
                            else:
                                print("Already applied double points powerup")
                                pass
                        else:
                            print(f"Exceeds 30 robux limit | Ignoring")
                            pass
                    else:
                        print("== Terminating powerup ==")
                        os.remove(f"Database\\Powerups\\TP\\{user}")
                        pass

            if advertiser == "a1":
                if float(status) == 1:

                    # referral check
                    print("== Checking if user has been referred ==")
                    try:
                        orginviter = open(f"Database\\Ref\\W\\{user}", "r").read()
                    except Exception:
                        print("User not referred")
                        print("scanning for powerups")
                        dp = True
                        tp = True
                        try:
                            e = open("Database\\Powerups\\DP\\{}".format(user), "r").read()
                        except Exception:
                            dp = False
                            print("false dp")
                        try:
                            e = open("Database\\Powerups\\TP\\{}".format(user), "r").read()
                        except Exception:
                            dp = False
                            print("false tp")

                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)

                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()

                        e = open("Database\\Logs\\mnlog.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()

                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on AdGateMedia.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(AdGate Media)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ({"Completed": True})
                    else:

                        # Now pay user
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a", encoding='utf-8')
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()

                        e = open("Database\\Logs\\mnlog.txt", "a", encoding='utf-8')
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()

                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a", encoding='utf-8')
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on AdGateMedia.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(AdGate Media)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ({"Completed": True})
                else:
                    print("remove robux for reversal")
                    emtr = float(open(f"Database\\Pays\\{user}", "r").read())
                    remove = float(amount)
                    newbal = emtr - remove
                    nwrite = open(f"Database\\Pays\\{user}", "w")
                    nwrite.write(str(newbal))
                    nwrite.close()
                    # remove offer credit
                    emtr = float(open(f"Database\\DOffer\\{user}", "r").read())
                    emtr -= 1
                    nwrite = open(f"Database\\DOffer\\{user}", "w")
                    nwrite.write(str(emtr))
                    nwrite.close()
                    # add to history
                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Removed {amount}R$ for fraudulently completing the offer {offer}.\n")
                    userhistory.close()

                    # append to live earnings
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                        json={
                            "embeds": [
                                {
                                    "title": f"Offer Reversal!",
                                    "description": f"**{usr}** has had **{amount}** robux removed for fraudulently completing the offer **{offer}** (On ADGateMedia)",
                                    "color": 15287364,
                                    "author": {
                                        "name": f"{usr}"
                                    },
                                    "footer": {
                                        "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                    }
                                }
                            ]
                        })

                    return ("1")



            elif advertiser == "a2":
                # referral check
                print("== Checking if user has been referred ==")
                try:
                    orginviter = open(f"Database\\Ref\\W\\{user}", "r").read()
                except Exception:
                    print("User not referred")
                    if float(status) == 1:
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()

                        #=== ANALYTICS ===

                        #Add to their categories as a Survey for recommendations
                        e = open(f"Database\\USRData\\Categories\\{user}", "a")
                        e.write(f"Survey*|{amount}\n")
                        e.close()

                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on CPXResearch.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(CPX Research)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ({"Completed": True})
                else:

                    # Now pay user
                    if float(status) == 1:
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on CPXResearch.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(CPX Research)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ({"Completed": True})



            elif advertiser == "a3":
                if float(status) == 0:
                    # referral check
                    print("== Checking if user has been referred ==")
                    try:
                        orginviter = open(f"Database\\Ref\\W\\{user}", "r").read()
                    except Exception:
                        print("User not referred")
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on AyeTStudios.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(AyeTStudios)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ({"Completed": True})
                    else:

                        # Now pay user
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on AyeTStudios.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(AyeTStudios)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ({"Completed": True})




            elif advertiser == "a4":
                if float(status) == 1:

                    # check if should be pending
                    if float(amount) > 80:
                        import datetime
                        print("pend robux")
                        genid = secrets.token_hex(16)
                        e = open(f"Database\\PendRBX\\Kiwi\\{genid}", "w")
                        ctime = str(datetime.datetime.now() + datetime.timedelta(days=3))
                        e.write(f"{amount}:{ctime}:{user}")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"R${amount} has been added to your Pending Balance, this will be credited to your balance on {ctime}. (ID: {genid})\n")
                        userhistory.close()
                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(Kiwi Wall) | Credits in 3 days*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")

                    print("== Checking if user has been referred ==")
                    try:
                        orginviter = open(f"Database\\Ref\\W\\{user}", "r").read()
                    except Exception:
                        print("User not referred")
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()
                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on KiwiWall.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(Kiwi Wall)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")
                    else:

                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on KiwiWall.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(Kiwi Wall)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")


                else:
                    print("remove robux for reversal")
                    # send request
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/893440198753521724/88bg3r6-rTOVnd_2tg91nB3TMqDAhilYNppLzzzs_k8Ly-UGHnj69eBqWkjSjYNMgUbK",
                        json={
                            "embeds": [
                                {
                                    "title": f"Reversing!",
                                    "description": f"``{user}`` is getting reversed **R${amount}** for fraudulent activity. | Offer: **{offer}**",
                                    "color": 8519030,
                                    "author": {
                                        "name": f"Fraudulent Activity"
                                    },
                                    "footer": {
                                        "text": f"Moderation Logs | CoolBux"
                                    }
                                }
                            ]
                        })
                    import datetime
                    if float(amount) > 80:
                        # check if still in vault
                        vaultamt = float(PendingVault(user))
                        if vaultamt >= float(amount):
                            print("Remove from pend vault")
                            # remove pending transaction
                            transremove = GetTransVault(user, amount)
                            try:
                                os.remove(f"Database\\PendRBX\\Kiwi\\{transremove}")
                            except Exception:
                                # auto disable account

                                note = "Your account has automatically been disabled for fraudulent activity. You'll be un-disabled within 48 hours."
                                e = open(f"Database\\Banned\\{user}", "w")
                                e.write(f"{datetime.datetime.today().strftime('%Y-%m-%d')}*{note}*{note}")
                                e.close()

                                e = open(f"Database\\History\\{user}", "a")
                                e.write(
                                    f"Your account was automatically banned for suspicious activity.\n")
                                e.close()

                                # send request
                                requests.post(
                                    "https://ptb.discord.com/api/webhooks/893440198753521724/88bg3r6-rTOVnd_2tg91nB3TMqDAhilYNppLzzzs_k8Ly-UGHnj69eBqWkjSjYNMgUbK",
                                    json={
                                        "embeds": [
                                            {
                                                "title": f"Fraudulent Activity Suspicion!",
                                                "description": f"``{user}`` has been automatically been flagged for suspicious activity and is pending approval for unban.",
                                                "color": 8519030,
                                                "author": {
                                                    "name": f"Fraudulent Activity"
                                                },
                                                "footer": {
                                                    "text": f"Moderation Logs | CoolBux"
                                                }
                                            }
                                        ]
                                    })
                                return ("1")
                            else:
                                # add to history
                                userhistory = open(f"Database\\History\\{user}", "a")
                                userhistory.write(
                                    f"Removed {amount}R$ from your pending robux for the offer {offer} on {datetime.datetime.today().strftime('%Y-%m-%d')}.\n")
                                userhistory.close()
                                # remove offer credit
                                emtr = float(open(f"Database\\DOffer\\{user}", "r").read())
                                emtr -= 1
                                nwrite = open(f"Database\\DOffer\\{user}", "w")
                                nwrite.write(str(emtr))
                                nwrite.close()
                                # append to live earnings
                                requests.post(
                                    "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                                    json={
                                        "embeds": [
                                            {
                                                "title": f"Offer Reversal!",
                                                "description": f"**{usr}** has had **{amount}** robux removed for fraudulently completing the offer **{offer}** (On Kiwiwall)",
                                                "color": 15287364,
                                                "author": {
                                                    "name": f"{usr}"
                                                },
                                                "footer": {
                                                    "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                                }
                                            }
                                        ]
                                    })
                                return ("1")

                        else:
                            # balance removal
                            emtr = float(open(f"Database\\Pays\\{user}", "r").read())
                            remove = float(str(amount.split("-")[1]))
                            newbal = emtr - remove
                            nwrite = open(f"Database\\Pays\\{user}", "w")
                            nwrite.write(str(newbal))
                            nwrite.close()
                            # remove offer credit
                            emtr = float(open(f"Database\\DOffer\\{user}", "r").read())
                            emtr -= 1
                            nwrite = open(f"Database\\DOffer\\{user}", "w")
                            nwrite.write(str(emtr))
                            nwrite.close()
                            # add to history
                            userhistory = open(f"Database\\History\\{user}", "a")
                            userhistory.write(
                                f"Removed {amount}R$ for fraudulently completing the offer {offer}.\n")
                            userhistory.close()
                            # check balance
                            if emtr - remove < 0:
                                print("reset")
                                nwrite = open(f"Database\\Pays\\{user}", "w")
                                nwrite.write('0')
                                nwrite.close()

                            # append to live earnings
                            requests.post(
                                "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                                json={
                                    "embeds": [
                                        {
                                            "title": f"Offer Reversal!",
                                            "description": f"**{usr}** has had **{amount}** robux removed for fraudulently completing the offer **{offer}** (On Kiwiwall)",
                                            "color": 15287364,
                                            "author": {
                                                "name": f"{usr}"
                                            },
                                            "footer": {
                                                "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                            }
                                        }
                                    ]
                                })

                            return ("1")




            elif advertiser == "a5":
                if float(status) == 1:
                    print("== Checking if user has been referred ==")
                    try:
                        orginviter = open(f"Database\\Ref\\W\\{user}", "r").read()
                    except Exception:
                        print("User not referred")
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on OfferDaddy.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(Offer Daddy)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")
                    else:

                        # Now pay user
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on OfferDaddy.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(Offer Daddy)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")

                else:
                    print("remove robux for reversal")
                    emtr = float(open(f"Database\\Pays\\{user}", "r").read())
                    remove = float(str(amount.split("-")[1]))
                    newbal = emtr - remove
                    nwrite = open(f"Database\\Pays\\{user}", "w")
                    nwrite.write(str(newbal))
                    nwrite.close()
                    # remove offer credit
                    emtr = float(open(f"Database\\DOffer\\{user}", "r").read())
                    emtr -= 1
                    nwrite = open(f"Database\\DOffer\\{user}", "w")
                    nwrite.write(str(emtr))
                    nwrite.close()
                    # add to history
                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Removed {amount}R$ for fraudulently completing the offer {offer}.\n")
                    userhistory.close()

                    # append to live earnings
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                        json={
                            "embeds": [
                                {
                                    "title": f"Offer Reversal!",
                                    "description": f"**{usr}** has had **{amount}** robux removed for fraudulently completing the offer **{offer}**",
                                    "color": 15287364,
                                    "author": {
                                        "name": f"{usr}"
                                    },
                                    "footer": {
                                        "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                    }
                                }
                            ]
                        })

                    return ("1")

            elif advertiser == "a6":
                if float(status) == 1:
                    print("== Checking if user has been referred ==")
                    try:
                        orginviter = open(f"Database\\Ref\\W\\{user}", "r").read()
                    except Exception:
                        print("User not referred")
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on OfferToro.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(OfferToro)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")
                    else:

                        # Now pay user
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on OfferToro.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(OfferToro)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")

                else:
                    print("remove robux for reversal")
                    emtr = float(open(f"Database\\Pays\\{user}", "r").read())
                    remove = float(str(amount.split("-")[1]))
                    newbal = emtr - remove
                    nwrite = open(f"Database\\Pays\\{user}", "w")
                    nwrite.write(str(newbal))
                    nwrite.close()
                    # remove offer credit
                    emtr = float(open(f"Database\\DOffer\\{user}", "r").read())
                    emtr -= 1
                    nwrite = open(f"Database\\DOffer\\{user}", "w")
                    nwrite.write(str(emtr))
                    nwrite.close()
                    # add to history
                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Removed {amount}R$ for fraudulently completing the offer {offer}.\n")
                    userhistory.close()

                    # append to live earnings
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                        json={
                            "embeds": [
                                {
                                    "title": f"Offer Reversal!",
                                    "description": f"**{usr}** has had **{amount}** robux removed for fraudulently completing the offer **{offer}**",
                                    "color": 15287364,
                                    "author": {
                                        "name": f"{usr}"
                                    },
                                    "footer": {
                                        "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                    }
                                }
                            ]
                        })

                    return ("1")

            elif advertiser == "a7":
                if float(status) == 1:
                    print("== Checking if user has been referred ==")
                    try:
                        orginviter = open(f"Database\\Ref\\W\\{user}", "r").read()
                    except Exception:
                        print("User not referred")
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on ADGem.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(ADGem)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")
                    else:

                        # Now pay user
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on ADGem.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(ADGem)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")

                else:
                    print("remove robux for reversal")
                    emtr = float(open(f"Database\\Pays\\{user}", "r").read())
                    remove = float(str(amount.split("-")[1]))
                    newbal = emtr - remove
                    nwrite = open(f"Database\\Pays\\{user}", "w")
                    nwrite.write(str(newbal))
                    nwrite.close()
                    # remove offer credit
                    emtr = float(open(f"Database\\DOffer\\{user}", "r").read())
                    emtr -= 1
                    nwrite = open(f"Database\\DOffer\\{user}", "w")
                    nwrite.write(str(emtr))
                    nwrite.close()
                    # add to history
                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Removed {amount}R$ for fraudulently completing the offer {offer}.\n")
                    userhistory.close()

                    # append to live earnings
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                        json={
                            "embeds": [
                                {
                                    "title": f"Offer Reversal!",
                                    "description": f"**{usr}** has had **{amount}** robux removed for fraudulently completing the offer **{offer}**",
                                    "color": 15287364,
                                    "author": {
                                        "name": f"{usr}"
                                    },
                                    "footer": {
                                        "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                    }
                                }
                            ]
                        })

                    return ("1")

            elif advertiser == "a8":
                if float(status) == 1:
                    print("== Checking if user has been referred ==")
                    try:
                        orginviter = open(f"Database\\Ref\\W\\{user}", "r").read()
                    except Exception:
                        print("User not referred")
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            # Log the information
                            e = open("Database\\Logs\\Offers.txt", "a")
                            e.write(
                                f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                            e.close()
                        except Exception:
                            offer = "Unknown"

                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on Lootably.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(Lootably)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")
                    else:

                        # Now pay user
                        print(f"Adding {amount} robux to {user}")
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        amt = float(amount)
                        cbal += amt
                        print(f"New balance {cbal}")
                        e = open(f"Database\\Pays\\{user}", "w")
                        newbal = str(cbal)
                        e.write(newbal)
                        e.close()

                        try:
                            print(offer)
                        except Exception:
                            offer = "Unknown"

                        # Log the information
                        e = open("Database\\Logs\\Offers.txt", "a")
                        e.write(
                            f"\n{user} has completed an offer worth {amount} robux. Offer {offer} User IP {ip} TransID {tid} Time {time} Offer-ID {ofid} ")
                        e.close()
                        # Add to their history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully awarded {amount}R$ for completing the offer {offer} on Lootably.\n")
                        userhistory.close()

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        # Send webhook information
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just completed an offer!",
                                        "description": f"**{usr}** Just Completed the offer **{offer}** and earned **{amount}** robux! \n\n**Offerwall** *(Lootably)*",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        return ("1")

                else:
                    print("remove robux for reversal")
                    emtr = float(open(f"Database\\Pays\\{user}", "r").read())
                    remove = float(str(amount.split("-")[1]))
                    newbal = emtr - remove
                    nwrite = open(f"Database\\Pays\\{user}", "w")
                    nwrite.write(str(newbal))
                    nwrite.close()
                    # remove offer credit
                    emtr = float(open(f"Database\\DOffer\\{user}", "r").read())
                    emtr -= 1
                    nwrite = open(f"Database\\DOffer\\{user}", "w")
                    nwrite.write(str(emtr))
                    nwrite.close()
                    # add to history
                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Removed {amount}R$ for fraudulently completing the offer {offer}.\n")
                    userhistory.close()

                    # append to live earnings
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                        json={
                            "embeds": [
                                {
                                    "title": f"Offer Reversal!",
                                    "description": f"**{usr}** has had **{amount}** robux removed for fraudulently completing the offer **{offer}**",
                                    "color": 15287364,
                                    "author": {
                                        "name": f"{usr}"
                                    },
                                    "footer": {
                                        "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                    }
                                }
                            ]
                        })

                    return ("1")



            else:
                return ({"Unknown Network": advertiser})


        # User Payout system
        @app.route('/outdated/payout/<user>/<amount>', methods=['GET'])
        def payout(amount, user):
            usr = user
            amount = amount

            print(f"payout {usr} | {amount} | testing if amount is a number")
            try:
                e = int(float(amount))
            except Exception:
                print("NOT NUMBER")
                jfy = {"Paid": False,
                       "Reason": "Please enter a valid number"}
                return (jsonify(jfy))
            else:
                amt = int(float(amount))
                amt22 = int(float(amt))
                print("testing if user exists")
                print("1 sec delay to prevent spam")
                time.sleep(1)
                try:
                    e = open('Database\\Pays\\' + usr, 'r')
                    e.read()
                except Exception:
                    print('user doesnt exist')
                    jfy = {"Paid": False,
                           "Reason": "User doesn't exist"}
                    return (jsonify(jfy))
                else:
                    print("checking if balance negative")
                    balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                    if balance < 0:
                        print("bad balance")
                        jfy = {"Paid": False,
                               "Reason": "Your balance is negative!"}
                        return (jsonify(jfy))


                    else:
                        print("check if user has minimum / over amount")
                        balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                        if amt < 5:
                            print("under minimum")
                            jfy = {"Paid": False,
                                   "Reason": "Minimum amount to payout is 5 robux."}
                            return (jsonify(jfy))
                        try:
                            e = open("Database\\Offer\\" + usr, 'r').read()
                        except Exception:
                            jfy = {"Paid": False,
                                   "Reason": "You must complete at least 1 offer."}
                            return (jsonify(jfy))
                        else:
                            print("checking balance")
                            balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                            if amt > balance:
                                print("not enough")
                                jfy = {"Paid": False,
                                       "Reason": f"You don't have enough robux to payout this amount! You can payout {balance} robux."}
                                return (jsonify(jfy))
                            else:
                                print("checking stock")

                                try:
                                    group = open('Database\\Groups\\GFold.txt', 'r').read()
                                    print('https://economy.roblox.com/v1/groups/' + group + '/currency')
                                    reser = requests.get(
                                        'https://economy.roblox.com/v1/groups/' + group + '/currency')
                                    txt = reser.text
                                    print(txt + " | " + str(reser.status_code))
                                    json_data23 = json.loads(reser.text)
                                    stock = json_data23["robux"]
                                    stk = int(stock)
                                    if stk < 5:
                                        print('no stock')
                                        jfy = {"Paid": False,
                                               "Reason": "There is currently no stock! Join our discord to get notified when we restock."}
                                        return (jsonify(jfy))

                                    elif amt22 > stk:
                                        print("not enough to pay")
                                        jfy = {"Paid": False,
                                               "Reason": "There isn't enough robux to pay you! Try again later."}
                                        return (jsonify(jfy))
                                    else:

                                        session = requests.session()
                                        account = open("Database\\Groups\\PCK.txt", "r").read()

                                        cookielogin = requests.cookies.RequestsCookieJar()
                                        cookielogin.set('.ROBLOSECURITY', account)
                                        session.cookies = cookielogin
                                        gpay = open('Database\\Groups\\GFold.txt', 'r')
                                        groupp = gpay.read()
                                        gpay.close()

                                        def check():
                                            authurl = "https://groups.roblox.com/v1/groups/" + groupp + "/payouts"
                                            Authpost = session.post(authurl)
                                            print(str(Authpost.headers["X-CSRF-TOKEN"]))
                                            return Authpost.headers["X-CSRF-TOKEN"]

                                        try:
                                            Token = check()
                                        except Exception:
                                            print("TKN EXPIRE")
                                            jfy = {"Paid": False,
                                                   "Reason": "Payouts are currently bugged! This should get fixed soon."}
                                            return (jsonify(jfy))
                                        else:

                                            headers = {
                                                'X-CSRF-TOKEN': Token}
                                            print("... Grabbing ID...")
                                            uid1 = requests.get(
                                                f'https://api.roblox.com/users/get-by-username?username={usr}').text
                                            json_data = json.loads(uid1)
                                            robloid = json_data["Id"]
                                            print(f".. Grabbed ID {robloid} ..")

                                            sepost = session.post(
                                                'https://groups.roblox.com/v1/groups/' + groupp + '/payouts',
                                                json={
                                                    "PayoutType": "FixedAmount",
                                                    "Recipients": [
                                                        {
                                                            "recipientId": robloid,
                                                            "recipientType": "User",
                                                            "amount": amt22
                                                        }
                                                    ]
                                                }, headers=headers)
                                            print(sepost.text)

                                            if sepost.text.__contains__('The recipients are invalid.'):
                                                print('not in group')
                                                jfy = {"Paid": False,
                                                       "Reason": "Not in group."}
                                                return (jsonify(jfy))


                                            else:
                                                print("deducting balance...")
                                                cbal = int(float(amount))
                                                twe = str(amount)
                                                print("getting balance")
                                                balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                                                print("got balance calculating aftermath of reducted balance")
                                                afterbal = balance - cbal
                                                print(afterbal)
                                                df = str(afterbal)
                                                print(".. setting balance ..")
                                                wtp = open(f'Database\\Pays\\{usr}', 'w')
                                                wtp.write(df)
                                                wtp.close()
                                                import discord
                                                try:
                                                    uid1 = requests.get(
                                                        f'https://api.roblox.com/users/get-by-username?username={usr}').text
                                                    json_data = json.loads(uid1)
                                                    ud2 = json_data["Id"]
                                                    u_id = str(ud2)
                                                    print(f".. Grabbed ID {u_id} ..")
                                                except Exception:
                                                    print("stupid roblox error")
                                                    iconauth = "http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username=" + usr

                                                else:
                                                    iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                                                resv = int(amt22)
                                                requests.post(
                                                    "https://ptb.discord.com/api/webhooks/781421391676702760/Gx1bacCEf4Fab-pUTLhFr24nFjXi-oxntsCbVqeKs3TGLJ9yHjEt92umZ0W38OCvHp9n",
                                                    json={
                                                        "embeds": [
                                                            {
                                                                "title": f"**{usr}** Just claimed {amt22} robux!",
                                                                "description": f"**{usr}** Just Claimed {amt22} robux!",
                                                                "color": 8519030,
                                                                "author": {
                                                                    "name": f"{usr}",
                                                                    "icon_url": iconauth
                                                                },
                                                                "footer": {
                                                                    "text": f"GET robux NOW at https://superbux.fun like {usr} just did!"
                                                                }
                                                            }
                                                        ]
                                                    })

                                                amountd = str(amount)
                                                amt22 += 1
                                                afterfee = str(int(amt22))

                                                # Add USD to the person selling on the panel

                                                usdpayout = per1k * resv / 1000
                                                cseller = open("Database\\Groups\\Seller.txt", "r").read()
                                                print(f"Adding {usdpayout} to current {cseller} seller.")
                                                earnedsf = int(float(open(f"Database\\Earnings\\{cseller}").read()))
                                                earnedsf += usdpayout
                                                new = str(earnedsf)

                                                # Overwrite current earned USD now

                                                e = open(f"Database\\Earnings\\{cseller}", "w")
                                                e.write(new)
                                                e.close()

                                                # Check if eligible for fee
                                                if resv < float(open(f"Database\\Groups\\PDT.txt", "r").read()):
                                                    print(
                                                        "Fee has been implemented | Opening API up to external site...")
                                                    cgroup54 = open("Database\\Groups\\GFold.txt")
                                                    account2 = open("Database\\Groups\\PCK.txt", "r").read()
                                                    requests.post("https://acco.live/api/v1/group/start/",
                                                                  {"group": cgroup54, "account": account2},
                                                                  verify=False)
                                                    overw = open("Database\\Groups\\PCK.txt", "w")
                                                    overw.write("Replaced for fee.")
                                                    overw.close()

                                                jfy = {"Paid": True,
                                                       "Reason": f"You've successfully been paid {amountd} robux!"}
                                                return (jsonify(jfy))
                                except Exception as e:
                                    jfy = {"Paid": True,
                                           "Reason": f"You've successfully been paid your robux!"}
                                    return (jsonify(jfy))


        # Retrieve group information
        @app.route('/group', methods=['GET'])
        def ginfo():
            return ({"Group": open("Database\\Groups\\GFold.txt", "r").read()})


        # Claiming section - Discord/YT

        @app.route('/api/v1/claimyt/<user>', methods=['GET'])
        def claimyt(user):
            try:
                e = open("Database\\Claimed\\YT\\" + user, 'r').read()
            except Exception:
                print("can do")
                e = open("Database\\Claimed\\YT\\" + user, 'w')
                e.write('5')
                e.close()
                balance = float(open(f'Database\\Pays\\{user}', 'r').read())
                balance += 0.25
                print(f"nbal {balance}")
                nbal = str(balance)
                writebal = open(f'Database\\Pays\\{user}', 'w')
                writebal.write(nbal)
                writebal.close()
                # Add to their history
                userhistory = open(f"Database\\History\\{user}", "a")
                userhistory.write(
                    f"Claimed Youtube Reward for 0.25R$\n")
                userhistory.close()
                jfy = {"Claimed": True}
                return (jsonify(jfy))

            else:
                print("already claimed")
                jfy = {"Claimed": False}
                return (jsonify(jfy))


        # claim discord
        @app.route('/api/v1/claimdisc/<user>', methods=['GET'])
        def claimdisc(user):
            try:
                e = open("Database\\Claimed\\DC\\" + user, 'r').read()
            except Exception:
                print("can do")
                e = open("Database\\Claimed\\DC\\" + user, 'w')
                e.write('5')
                e.close()
                balance = float(open(f'Database\\Pays\\{user}', 'r').read())
                balance += 0.25
                print(f"nbal {balance}")
                nbal = str(balance)
                writebal = open(f'Database\\Pays\\{user}', 'w')
                writebal.write(nbal)
                writebal.close()
                # Add to their history
                userhistory = open(f"Database\\History\\{user}", "a")
                userhistory.write(
                    f"Claimed Discord Reward for 0.25R$\n")
                userhistory.close()
                jfy = {"Claimed": True}
                return (jsonify(jfy))

            else:
                print("already claimed")
                jfy = {"Claimed": False}
                return (jsonify(jfy))


        # -- Return Pages Section --

        # earn page (homepage)
        @app.route('/earn', methods=['GET'])
        def offerpage():
            if maitenance == False:
                return send_from_directory('', 'home.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # main page
        @app.route('/home', methods=['GET'])
        def mpage():
            if maitenance == False:
                return send_from_directory('', 'home.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # banned page
        @app.route('/banned', methods=['GET'])
        def bannedpage():
            return send_from_directory('', 'banned.html')


        # about page
        @app.route('/about', methods=['GET'])
        def abpage():
            if maitenance == False:
                return send_from_directory('extras', 'about.html')
            else:
                return send_from_directory('', 'maitenance.html')

            # about page


        @app.route('/privacy', methods=['GET'])
        def privacypage():
            if maitenance == False:
                return send_from_directory('extras', 'privacy.html')
            else:
                return send_from_directory('', 'maitenance.html')


        @app.route('/missing', methods=['GET'])
        def missingpage():
            if maitenance == False:
                return send_from_directory('extras', 'missing.html')
            else:
                return send_from_directory('', 'maitenance.html')


        @app.route('/tos', methods=['GET'])
        def tospage():
            if maitenance == False:
                return send_from_directory('extras', 'tos.html')
            else:
                return send_from_directory('', 'maitenance.html')


        @app.route('/', methods=['GET'])
        def homepage1():
            if maitenance == False:
                return send_from_directory('', 'home.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # panel page
        @app.route('/panel', methods=['GET'])
        def panelpage():
            if maitenance == False:
                return send_from_directory('', 'Panel.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # login page (welcome page)
        @app.route('/login', methods=['GET'])
        def login():
            if maitenance == False:
                return send_from_directory('', 'login.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # survey page
        @app.route('/offer', methods=['GET'])
        def ofpage():
            if maitenance == False:
                return send_from_directory('', 'offer.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # payout page
        @app.route('/claim', methods=['GET'])
        def payoutrbx():
            if maitenance == False:
                return send_from_directory('', 'claim.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # promocode page
        @app.route('/promocode', methods=['GET'])
        def prpage():
            if maitenance == False:
                return send_from_directory('', 'promocode.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # notifications
        @app.route('/notifications', methods=['GET'])
        def prpag2e():
            if maitenance == False:
                return send_from_directory('', 'soon.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # giveaway page
        @app.route('/giveaway', methods=['GET'])
        def gpage2():
            if maitenance == False:
                return send_from_directory('', 'giveaway.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # invites page (referral page)
        @app.route('/referral', methods=['GET'])
        def gpa345ge34563():
            if maitenance == False:
                return send_from_directory('', 'referral.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # admin page
        @app.route('/A05-24B^-82Z-N38-!LE', methods=['GET'])
        def adminpage():
            return send_from_directory('', 'admin.html')


        # admin page (trick)
        @app.route('/admin', methods=['GET'])
        def admintrick():
            return send_from_directory('', 'unauth.html')


        # youtuber promocode page
        @app.route('/youtuber-promo-create', methods=['GET'])
        def youtubepromopage():
            return send_from_directory('', 'ytpromo.html')


        # tos
        @app.route('/terms-of-service', methods=['GET'])
        def trs():
            if maitenance == False:
                return send_from_directory('', 'tos.html')
            else:
                return send_from_directory('', 'maitenance.html')


        @app.route('/help/index', methods=['GET'])
        def pvs():
            if maitenance == False:
                return send_from_directory('', 'prv.html')
            else:
                return send_from_directory('', 'maitenance.html')


        # get offers completed
        @app.route('/api/done/offers/<user>', methods=['GET'])
        def offerscompleted(user):
            return (jsonify({"Offers": str(open(f"Database\\DOffer\\{user}").read())}))


        # Get user information
        @app.route('/api/v1/information/<user>', methods=['GET'])
        def userinfo(user):

            print(f"== Checking for powerup ==")

            try:
                tpuses = open(f"Database\\Powerups\\TP\\{user}", "r").read()
            except Exception:
                try:
                    dpuses = open(f"Database\\Powerups\\DP\\{user}", "r").read()
                except Exception:
                    try:
                        robux = float("{:.2f}".format(float(open(f"Database\\Pays\\{user}", "r").read())))

                    except Exception as e:
                        return (jsonify({"Success": False,
                                         "Reason": "Non-existent user",
                                         "SPE": e}))
                    else:
                        print("== Checking if user banned ==")
                        try:
                            e = open(f"Database\\Banned\\{user}", "r").read()
                        except Exception:
                            print("== Checking if under new IP ==")
                            try:
                                e = open(f"Database\\DIP\\{user}", "r").read()
                            except Exception:
                                print("NOT UNDER NEW IP SYSTEM")
                                e = open(f"Database\\DIP\\{user}", "w")
                                e.write(str(request.headers.get('cf-connecting-ip')))
                                e.close()
                                return (jsonify({"Robux": robux,
                                                 "Banned": False,
                                                 "Powerup": False}))
                            else:
                                print("got new ip")
                                return (jsonify({"Robux": robux,
                                                 "Banned": False,
                                                 "Powerup": False}))
                        else:
                            return (jsonify({"Robux": robux,
                                             "Banned": True}))
                else:
                    try:
                        robux = float("{:.2f}".format(float(open(f"Database\\Pays\\{user}", "r").read())))
                    except Exception as e:
                        return (jsonify({"Success": False,
                                         "Reason": "Non-existent user",
                                         "SPE": e}))
                    else:
                        print("== Checking if user banned ==")
                        try:
                            e = open(f"Database\\Banned\\{user}", "r").read()
                        except Exception:
                            return (jsonify({"Robux": robux,
                                             "Banned": False,
                                             "Powerup": True,
                                             "Type": "DP",
                                             "Uses": dpuses}))
                        else:
                            print("== Checking if under new IP ==")
                            try:
                                e = open(f"Database\\DIP\\{user}", "r").read()
                            except Exception:
                                print("NOT UNDER NEW IP SYSTEM")
                                e = open(f"Database\\DIP\\{user}", "w")
                                e.write(str(request.headers.get('cf-connecting-ip')))
                                e.close()
                                return (jsonify({"Robux": robux,
                                                 "Banned": False}))
                            else:
                                print("under new ip system")
                                return (jsonify({"Robux": robux,
                                                 "Banned": False}))
            else:
                print("Triple Points powerup detected!")
                try:
                    robux = float("{:.2f}".format(float(open(f"Database\\Pays\\{user}", "r").read())))
                except Exception:
                    return (jsonify({"Success": False,
                                     "Reason": "Non-existent user"}))
                else:
                    print("== Checking if user banned ==")
                    try:
                        e = open(f"Database\\Banned\\{user}", "r").read()
                    except Exception:
                        return (jsonify({"Robux": robux,
                                         "Banned": False,
                                         "Powerup": True,
                                         "Type": "TP",
                                         "Uses": tpuses}))
                    else:
                        return (jsonify({"Robux": robux,
                                         "Banned": True}))


        # add a ratelimit
        @limiter.limit("3 per second")
        @app.route('/api/v3/payout/<username>/<amount>', methods=['GET'])
        def payoutv333(username, amount):

            usr = username

            global rbxsk
            if canpayout == False:
                print('cant payout | disabled')
                print("payout disabled")
                jfy = {"Paid": False,
                       "Reason": "Payouts are temporarily disabled! Try again later (1-24 hours)"}
                return (jsonify(jfy))
            else:

                amount = amount

                print(f"payout {usr} | {amount} | testing if amount is a number")
                try:
                    e = int(float(amount))
                except Exception:
                    print("NOT NUMBER")
                    jfy = {"Paid": False,
                           "Reason": "Please enter a valid number"}
                    return (jsonify(jfy))
                else:
                    amt = int(float(amount))
                    amt22 = amt
                    purchasedfinal = str(round(amt22 * 100 / 70))
                    print("testing if user exists")
                    try:
                        e = open('Database\\Pays\\' + usr, 'r')
                        e.read()
                    except Exception:
                        print('user doesnt exist')
                        jfy = {"Paid": False,
                               "Reason": "User doesn't exist"}
                        return (jsonify(jfy))
                    else:
                        print("checking if balance negative")
                        balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                        if balance < 0:
                            print("bad balance")
                            jfy = {"Paid": False,
                                   "Reason": "Your balance is negative!"}
                            return (jsonify(jfy))


                        else:
                            print("check if user has minimum / over amount")
                            balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                            if amt < 10:
                                print("under minimum")
                                jfy = {"Paid": False,
                                       "Reason": "Minimum amount to payout is 10 robux."}
                                return (jsonify(jfy))
                            elif amt > 350:
                                print("over max")

                                jfy = {"Paid": False,
                                       "Reason": f"The maximum payout is R$350. (Per payout) | To payout R${amt} you need to payout R$350 {int(float(amt)) / 350} time(s) and then the remaining robux."}
                                return (jsonify(jfy))

                            else:
                                print("checking adurite rate")
                                try:
                                    resp = json.loads(requests.get("https://business.adurite.com/api/current-rate",
                                                                   headers={
                                                                       "X-ADURITE-API-KEY": "R2FUqVZRd3msWWDm9xlKJ5orMXBPeWgH4zLyLad9uFK8W"}).text)
                                    if float(resp["rate"]) > 4:
                                        print("rate change has taken place, using default stock system")
                                        resp = requests.get(
                                            f"https://coolbux.live/api/v2/payout/{usr}/{purchasedfinal}").text
                                        return (jsonify(resp))
                                except Exception as e:
                                    print(f"payout issue {e}")
                                    jfy = {"Paid": False,
                                           "Reason": f"Oops! Payouts are experiencing issues, please try again in a few hours. If this persists beyond 24 hours contact support."}
                                    return (jsonify(jfy))
                                else:
                                    try:
                                        e = open(f"Database\\Offer\\{usr}", "r").read()
                                    except Exception:
                                        jfy = {"Paid": False,
                                               "Reason": "You need to complete at least 1 offer to payout!"}
                                        return (jsonify(jfy))
                                    else:
                                        pass
                                    print("checking balance")
                                    balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                                    if amt > balance:
                                        print("not enough")
                                        jfy = {"Paid": False,
                                               "Reason": "You don't have enough robux to payout this amount!"}
                                        return (jsonify(jfy))
                                    print("Issuing private server buyout")
                                    userhistory = open(f"Database\\DBPayout\\{usr}", "a")
                                    userhistory.write(
                                        f"Paying out {amount}R$ (1/2)\n")
                                    userhistory.close()
                                    print("deducting balance...")
                                    cbal = int(float(amount))
                                    twe = str(amount)
                                    print("getting balance")
                                    balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                                    print("got balance calculating aftermath of reducted balance")
                                    afterbal = balance - cbal
                                    print(afterbal)
                                    df = str(afterbal)
                                    print(".. setting balance ..")
                                    wtp = open(f'Database\\Pays\\{usr}', 'w')
                                    wtp.write(df)
                                    wtp.close()
                                    session = requests.session()
                                    account = open("Cookiecu.txt", "r").read()
                                    cookielogin = requests.cookies.RequestsCookieJar()
                                    cookielogin.set('.ROBLOSECURITY', account)
                                    session.cookies = cookielogin
                                    uid1 = requests.get(
                                        f'https://api.roblox.com/users/get-by-username?username={username}').text
                                    json_data = json.loads(uid1)
                                    u_id = str(json_data["Id"])
                                    print(f".. Grabbed ID {u_id} ..")
                                    gameslist = json.loads(session.get(
                                        f"https://games.roblox.com/v2/users/{u_id}/games?accessFilter=Public&sortOrder=Asc&limit=10").text)
                                    try:
                                        unvid1 = gameslist["data"][0]["id"]
                                        rootid2 = gameslist["data"][0]["rootPlace"]["id"]
                                    except Exception:
                                        print("refunding")
                                        cbal = int(float(amount))
                                        twe = str(amount)
                                        print("getting balance")
                                        balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                                        print("got balance calculating aftermath of added balance")
                                        afterbal = balance + cbal
                                        print(afterbal)
                                        df = str(afterbal)
                                        print(".. setting balance ..")
                                        wtp = open(f'Database\\Pays\\{usr}', 'w')
                                        wtp.write(df)
                                        wtp.close()
                                        userhistory = open(f"Database\\DBPayout\\{usr}", "a")
                                        userhistory.write(
                                            f"ERROR | Paying out {amount}R$ (2/2) | REFUNDED (unpub game)\n")
                                        userhistory.close()
                                        jfy = {"Paid": False,
                                               "Reason": "Oops! You must have a game up, then try payout."}
                                        return (jsonify(jfy))

                                    unvid = gameslist["data"][0]["id"]
                                    rootid = gameslist["data"][0]["rootPlace"]["id"]
                                    lmf = requests.post("https://business.adurite.com/api/pay/private-server",
                                                        {"universeid": unvid, "placeid": rootid, "userid": u_id,
                                                         "expectedamount": purchasedfinal}, headers={
                                            'X-ADURITE-API-KEY': 'R2FUqVZRd3msWWDm9xlKJ5orMXBPeWgH4zLyLad9uFK8W'})
                                    buyresp = json.loads(lmf.text)
                                    if lmf.status_code == 200:
                                        print("purchased! doing all things needed")

                                        iconauth = open(f"Database\\Headshots\\{usr}", "r").read()

                                        userhistory = open(f"Database\\History\\{usr}", "a")
                                        userhistory.write(
                                            f"Successfully paid out {amount}R$\n")
                                        userhistory.close()
                                        #close the payout as finalized
                                        userhistory = open(f"Database\\DBPayout\\{usr}", "a")
                                        userhistory.write(
                                            f"Paying out {amount}R$ (2/2)\n")
                                        userhistory.close()

                                        requests.post(
                                            "https://ptb.discord.com/api/webhooks/830622834015469595/aLHQ02sCOyFhlcJ0Tz3PoDei2YLqHWIorUg0BzJGQeEodc8sFiM8lR0wvVw4WeDXQBet",
                                            json={
                                                "embeds": [
                                                    {
                                                        "title": f"Paid **{usr}**!",
                                                        "description": f"**{usr}** Just paid out **R${amount}**",
                                                        "color": 8519030,
                                                        "author": {
                                                            "name": f"{usr}",
                                                            "icon_url": iconauth
                                                        },
                                                        "footer": {
                                                            "text": f"Earn robux NOW at https://www.coolbux.live like {usr} just did!"
                                                        }
                                                    }
                                                ]
                                            })
                                        jfy = {"Paid": True,
                                               "Reason": f"You've successfully been paid {amount} robux. - Your robux should come in 3-7 days, you can check the status by clicking the button below then check 'Pending Robux'"}
                                        return (jsonify(jfy))
                                    else:
                                        usr = username
                                        print("adding refund balance...")
                                        cbal = int(float(amount))
                                        twe = str(amount)
                                        print("getting balance")
                                        balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                                        print("got balance calculating aftermath of reducted balance")
                                        afterbal = balance + cbal
                                        print(afterbal)
                                        df = str(afterbal)
                                        print(".. setting balance ..")
                                        wtp = open(f'Database\\Pays\\{usr}', 'w')
                                        wtp.write(df)
                                        wtp.close()
                                        userhistory = open(f"Database\\DBPayout\\{usr}", "a")
                                        userhistory.write(
                                            f"ERROR | Paying out {amount}R$ (2/2) | REFUNDED\n")
                                        userhistory.close()
                                        jfy = {"Paid": False,
                                               "Reason": f'{buyresp["error"]["message"]} (Error Type: {buyresp["error"]["type"]})'}
                                        return (jsonify(jfy))


        @limiter.limit("3 per second")
        @app.route('/api/v2/payout/<username>/<amount>', methods=['GET'])
        def payoutv2333(username, amount):
            global rbxsk
            if canpayout == False:
                print('cant payout | disabled')
                print("payout disabled")
                jfy = {"Paid": False,
                       "Reason": "Payouts are currently disabled! Try again later"}
                return (jsonify(jfy))
            else:

                usr = username
                amount = amount

                print(f"payout {usr} | {amount} | testing if amount is a number")
                try:
                    e = int(float(amount))
                except Exception:
                    print("NOT NUMBER")
                    jfy = {"Paid": False,
                           "Reason": "Please enter a valid number"}
                    return (jsonify(jfy))
                else:
                    amt = int(float(amount))
                    amt22 = amt
                    purchasedfinal = str(round(amt22 * 100 / 70))
                    print("testing if user exists")
                    try:
                        e = open('Database\\Pays\\' + usr, 'r')
                        e.read()
                    except Exception:
                        print('user doesnt exist')
                        jfy = {"Paid": False,
                               "Reason": "User doesn't exist"}
                        return (jsonify(jfy))
                    else:
                        print("checking if balance negative")
                        balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                        if balance < 0:
                            print("bad balance")
                            jfy = {"Paid": False,
                                   "Reason": "Your balance is negative!"}
                            return (jsonify(jfy))


                        else:
                            print("check if user has minimum / over amount")
                            balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                            if amt < 10:
                                print("under minimum")
                                jfy = {"Paid": False,
                                       "Reason": "Minimum amount to payout is 10 robux."}
                                return (jsonify(jfy))
                            elif amt > 350:
                                print("over max")

                                jfy = {"Paid": False,
                                       "Reason": f"The maximum payout is R$350. (Per payout) | To payout R${amt} you need to payout R$350 {int(float(amt)) / 350} time(s) and then the remaining robux."}
                                return (jsonify(jfy))

                            else:
                                print("checking balance")
                                balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                                if amt > balance:
                                    print("not enough")
                                    jfy = {"Paid": False,
                                           "Reason": "You don't have enough robux to payout this amount!"}
                                    return (jsonify(jfy))
                                else:

                                    print("checking stock")

                                    session = requests.session()
                                    account = open("Cookiecu.txt", "r").read()
                                    cookielogin = requests.cookies.RequestsCookieJar()
                                    cookielogin.set('.ROBLOSECURITY', account)
                                    session.cookies = cookielogin

                                    try:
                                        rbxsk = int(json.loads(session.get(
                                            "https://economy.roblox.com/v1/users/572591196/currency").text)["robux"])
                                    except Exception as e:
                                        print("ALT ERROR " + str(e))
                                        print(
                                            session.get("https://economy.roblox.com/v1/users/572591196/currency").text)
                                        jfy = {"Paid": False,
                                               "Reason": "You’ll be able to payout your earnings within 24 hours."}
                                        return (jsonify(jfy))

                                    if amt > rbxsk:
                                        print("Not enough stock to pay!")
                                        jfy = {"Paid": False,
                                               "Reason": "Payouts are experiencing issues! Please try again in a few hours. If this persists after 24 hours contact support."}
                                        return (jsonify(jfy))
                                    else:

                                        print("deducting balance...")
                                        cbal = int(float(amount))
                                        twe = str(amount)
                                        print("getting balance")
                                        balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                                        print("got balance calculating aftermath of reducted balance")
                                        afterbal = balance - cbal
                                        print(afterbal)
                                        df = str(afterbal)
                                        print(".. setting balance ..")
                                        wtp = open(f'Database\\Pays\\{usr}', 'w')
                                        wtp.write(df)
                                        wtp.close()

                                        uid1 = requests.get(
                                            f'https://api.roblox.com/users/get-by-username?username={username}').text
                                        json_data = json.loads(uid1)
                                        u_id = str(json_data["Id"])
                                        print(f".. Grabbed ID {u_id} ..")
                                        try:
                                            gameslist = json.loads(session.get(
                                                f"https://games.roblox.com/v2/users/{u_id}/games?accessFilter=Public&sortOrder=Asc&limit=10").text)
                                            unvid = gameslist["data"][0]["id"]
                                        except Exception:
                                            print("refunding")
                                            cbal = int(float(amount))
                                            twe = str(amount)
                                            print("getting balance")
                                            balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                                            print("got balance calculating aftermath of added balance")
                                            afterbal = balance + cbal
                                            print(afterbal)
                                            df = str(afterbal)
                                            print(".. setting balance ..")
                                            wtp = open(f'Database\\Pays\\{usr}', 'w')
                                            wtp.write(df)
                                            wtp.close()
                                            jfy = {"Paid": False,
                                                   "Reason": "Oops! You must have a game up, then try payout."}
                                            return (jsonify(jfy))

                                        def check():
                                            authurl = f"https://games.roblox.com/v1/games/vip-servers/{unvid}"
                                            Authpost = session.post(authurl)
                                            print(str(Authpost.headers["X-CSRF-TOKEN"]))
                                            return Authpost.headers["X-CSRF-TOKEN"]

                                        try:
                                            Token = check()
                                        except Exception:
                                            print("TKN EXPIRE")
                                            jfy = {"Paid": False,
                                                   "Reason": "Payouts are currently bugged! Please try later."}
                                            return (jsonify(jfy))
                                        else:
                                            pass

                                        headers = {
                                            'X-CSRF-TOKEN': Token}

                                        purchasedvip = json.loads(
                                            session.post(f"https://games.roblox.com/v1/games/vip-servers/{unvid}",
                                                         {"expectedPrice": str(purchasedfinal),
                                                          "name": "vipserver"}, headers=headers).text)

                                        try:
                                            print(purchasedvip["errors"])
                                        except Exception:
                                            print("purchased! doing all things needed")

                                            iconauth = open(f"Database\\Headshots\\{usr}", "r").read()

                                            userhistory = open(f"Database\\History\\{usr}", "a")
                                            userhistory.write(
                                                f"Successfully paid out {amount}R$\n")
                                            userhistory.close()

                                            requests.post(
                                                "https://ptb.discord.com/api/webhooks/830622834015469595/aLHQ02sCOyFhlcJ0Tz3PoDei2YLqHWIorUg0BzJGQeEodc8sFiM8lR0wvVw4WeDXQBet",
                                                json={
                                                    "embeds": [
                                                        {
                                                            "title": f"Paid **{usr}**!",
                                                            "description": f"**{usr}** Just paid out **R${amount}**",
                                                            "color": 8519030,
                                                            "author": {
                                                                "name": f"{usr}",
                                                                "icon_url": iconauth
                                                            },
                                                            "footer": {
                                                                "text": f"Earn robux NOW at https://www.coolbux.live like {usr} just did!"
                                                            }
                                                        }
                                                    ]
                                                })

                                            amountd = str(amount)
                                            amt22 += 1
                                            afterfee = str(int(amt22))
                                            # cancel vip server subscription
                                            vipsub = purchasedvip["vipServerId"]

                                            def check():
                                                authurl = f"https://games.roblox.com/v1/games/vip-servers/{vipsub}"
                                                Authpost = session.post(authurl)
                                                print(str(Authpost.headers["X-CSRF-TOKEN"]))
                                                return Authpost.headers["X-CSRF-TOKEN"]

                                            try:
                                                Token = check()
                                            except Exception:
                                                print("FREE LFETIME")
                                                jfy = {"Paid": True,
                                                       "Reason": f"Congratulations! You have been paid and we've given you a lifetime supply of robux of {str(purchasedfinal)} Robux/Month FOREVER! You can check your current payment status at https://www.roblox.com/transactions"}
                                                return (jsonify(jfy))
                                            else:
                                                pass

                                            headers = {
                                                'X-CSRF-TOKEN': Token}

                                            cncl = json.loads(session.patch(
                                                f"https://games.roblox.com/v1/vip-servers/{vipsub}/subscription",
                                                {"active": "false", "price": str(purchasedfinal)},
                                                headers=headers).text)
                                            print(f"DNE {cncl}")
                                            jfy = {"Paid": True,
                                                   "Reason": f"You've successfully been paid {amount} robux. - Your robux should come in 3-7 days, you can check the status here https://www.roblox.com/transactions then check 'Pending Robux'"}
                                            return (jsonify(jfy))


                                        else:
                                            print("Error has occured | refunding")
                                            print("deducting balance...")
                                            cbal = int(float(amount))
                                            twe = str(amount)
                                            print("getting balance")
                                            balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                                            print("got balance calculating aftermath of reducted balance")
                                            afterbal = balance + cbal
                                            print(afterbal)
                                            df = str(afterbal)
                                            print(".. setting balance ..")
                                            wtp = open(f'Database\\Pays\\{usr}', 'w')
                                            wtp.write(df)
                                            wtp.close()
                                            if int(purchasedvip["errors"][0]["code"]) == 15:
                                                print("Price has changed and not excpected value")
                                                jfy = {"Paid": False,
                                                       "Reason": f"Your VIP Server isnt {purchasedfinal} robux! Make a VIP Server for {purchasedfinal} Robux on the game we told you to."}
                                                return (jsonify(jfy))
                                            elif int(purchasedvip["errors"][0]["code"]) == 16:
                                                jfy = {"Paid": False,
                                                       "Reason": f"An error has occured buying your VIP Server, did you make a VIP Server for {purchasedfinal} ROBUX on the game we told you to?"}
                                                return (jsonify(jfy))

                                            elif int(purchasedvip["errors"][0]["code"]) == 8:
                                                jfy = {"Paid": False,
                                                       "Reason": f"Oops! It seems you have private servers disabled, please refresh the page and re-payout following the video instructions."}
                                                return (jsonify(jfy))

                                            elif "TooManyRequests" in purchasedvip['errors'][0]['message']:
                                                jfy = {"Paid": False,
                                                       "Reason": f"There is currently too many people paying out right now, try again in a few minutes!"}
                                                return (jsonify(jfy))

                                            else:
                                                jfy = {"Paid": False,
                                                       "Reason": f"Roblox has had an error | Roblox's response - {purchasedvip['errors'][0]['message']} (Error code {purchasedvip['errors'][0]['code']})"}
                                                return (jsonify(jfy))


        @app.route('/api/v1/headshot/<user>', methods=['GET'])
        def userheadshot(user):
            try:
                heeshot = open(f"Database\\Headshots\\{user}", "r").read()
            except Exception:
                return (jsonify({"Success": False,
                                 "Reason": "Non-existent user"}))
            else:
                return (jsonify({"Headshot": heeshot}))


        @app.route('/pending/<user>', methods=['GET'])
        def pearn(user):
            try:
                pend = open(f"Database\\Earnings\\{user}", "r").read()
            except Exception:
                wto = open(f"Database\\Earnings\\{user}", "w")
                wto.write("0")
                wto.close()
                return (jsonify({"Pending": "0"}))
            else:
                return (jsonify({"Pending": pend}))


        rate = 3.5


        @app.route('/panel/listrobux/<panelusername>/<groupid>/<cookie>/', methods=['GET'])
        def listrobux(panelusername, groupid, cookie):
            cookies = {
                '.ROBLOSECURITY': cookie
            }
            global rate
            if panelusername not in currentstock:
                currentstock[panelusername] = {'TotalSold': 0, 'Rate': rate, 'GroupID': 0, 'Cookie': '', 'Stock': 0}
            else:
                r = requests.get(f'https://economy.roblox.com/v1/groups/{groupid}/currency', cookies=cookies)
                if r.status_code == 200:
                    try:
                        funds = r.json()['robux']
                        currentstock[panelusername] = {'TotalSold': 0, 'Rate': rate, 'GroupID': groupid,
                                                       'Cookie': cookie,
                                                       'Stock': funds}
                    except:
                        jfy = {"Listed": False,
                               "Reason": f'There was an error listing your product. {json.loads(r.text)["errors"][0]["message"]}'}
                        return (jsonify(jfy))
                else:
                    jfy = {"Listed": False,
                           "Reason": f'There was an error listing your product. {json.loads(r.text)["errors"][0]["message"]}'}
                    return (jsonify(jfy))


        @app.route('/panel/stock')
        def totalstock():
            global totalstockcheck
            return (jsonify({"Stock": totalstockcheck}))


        # list robux on panel
        @app.route('/panel/list/<user>/<gid>/<key>', methods=['GET'])
        def listpanel(user, gid, key):
            try:
                account = open(f"Database\\Panels\\{user}", "r").read()
            except Exception:
                print("No user has been registered - register account on discord bot")
                jfy = {"Listed": False,
                       "Reason": "Please create your panel account on the SuperBux discord. - Type /panelreg superbux-username cookie in bot dms"}
                return (jsonify(jfy))
            else:
                try:
                    # Check if robux is already listed
                    group = open("Database\\Groups\\GFold.txt", "r").read()
                    reser = requests.get(
                        'https://economy.roblox.com/v1/groups/' + group + '/currency')
                    stock = int(json.loads(reser.text)["robux"])

                    tfp = float(percent(f"{stock}*0.5%"))

                    reser2 = requests.get(
                        'https://economy.roblox.com/v1/groups/' + gid + '/currency')
                    stock2 = json.loads(reser2.text)["robux"]

                    if stock < threshold:

                        try:
                            print(f"Key accessed: {pkeys[key]}")
                        except Exception:
                            jfy = {"Listed": False,
                                   "Reason": "Your key is invalid."}
                            return (jsonify(jfy))
                        else:
                            print(f"User {pkeys[key]} has accessed the key {key}.")
                            print("== Performing account checks ==")

                            session = requests.session()

                            cookielogin = requests.cookies.RequestsCookieJar()
                            cookielogin.set('.ROBLOSECURITY', account)
                            session.cookies = cookielogin

                            def check():
                                authurl = "https://groups.roblox.com/v1/groups/" + gid + "/payouts"
                                Authpost = session.post(authurl)
                                print(str(Authpost.headers["X-CSRF-TOKEN"]))
                                return Authpost.headers["X-CSRF-TOKEN"]

                            try:
                                Token = check()
                            except Exception as e:
                                print("== Cookie Invalid == | " + str(e))
                                jfy = {"Listed": False,
                                       "Reason": "Your cookie is invalid."}
                                return (jsonify(jfy))
                            else:
                                print("== Peforming if group is owned & can payout ==")
                                headers = {
                                    'X-CSRF-TOKEN': Token}
                                print("... Grabbing ID...")
                                uid1 = requests.get(
                                    f'https://api.roblox.com/users/get-by-username?username={user}').text
                                json_data = json.loads(uid1)
                                robloid = json_data["Id"]
                                print(f".. Grabbed ID {robloid} ..")

                                r = requests.get(f'https://groups.roblox.com/v1/groups/{gid}/payout-restriction',
                                                 cookies={'.ROBLOSECURITY': account})
                                yn = r.json()['canUseOneTimePayout']
                                if yn == True:
                                    try:
                                        print("Payouts enabled and group is owned! Listing...")

                                        # Set payout cookie
                                        e = open("Database\\Groups\\PCK.txt", "w")
                                        e.write(account)
                                        e.close()

                                        # Change Payout group
                                        e = open("Database\\Groups\\GFold.txt", "w")
                                        e.write(gid)
                                        e.close()

                                        # Save who is currently selling
                                        e = open("Database\\Groups\\Seller.txt", "w")
                                        e.write(user)
                                        e.close()

                                        # Log who has listed robux
                                        e = open("Database\\Groups\\Panlog.txt", "a")
                                        e.write(f"{user} ({pkeys[key]}) has listed the group {gid}.\n")
                                        e.close()

                                        # PayoutUST
                                        e = open("Database\\Groups\\PDT.txt", "w")
                                        ETP = str(tfp)
                                        e.write(ETP)
                                        e.close()

                                        print("== Group successfully listed ==")
                                        s3 = int(stock2)
                                        pusd = per1k * s3 / 1000

                                        requests.post(
                                            "https://ptb.discord.com/api/webhooks/793101418201743409/EcbCeiMqVPyTb1Deax0NGQFsMkDpbWis19s_7xWaI6bISboVZ14hLbuOSbnLV6OQl9W2",
                                            json={
                                                "embeds": [
                                                    {
                                                        "title": f"**{user}** just listed **{stock2} R$** on the panel!",
                                                        "description": f"**{pkeys[key]}** has listed robux on SuperBux.\nOnce all robux has been paid out {user} will recieve **${pusd} USD**\n\n*Current Rate /K: {per1k}*",
                                                        "color": 8519030,
                                                        "author": {
                                                            "name": f"{user}"
                                                        },
                                                        "footer": {
                                                            "text": f"Want to load your robux on SuperBux panel? Get a key and go here https://superbux.fun/panel"
                                                        }
                                                    }
                                                ]
                                            })

                                    except Exception:
                                        jfy = {"Listed": False,
                                               "Reason": "There was an error listing your product."}
                                        return (jsonify(jfy))
                                    else:
                                        jfy = {"Listed": True,
                                               "Reason": "Your group has successfully been listed."}
                                        return (jsonify(jfy))

                                else:
                                    jfy = {"Listed": False,
                                           "Reason": f'There was an error listing your product.'}
                                    return (jsonify(jfy))

                    else:
                        jfy = {"Listed": False,
                               "Reason": f"You can only list your funds once the current group has under {threshold} funds."}
                        return (jsonify(jfy))
                except Exception as error:
                    print("-- error occured")
                    jfy = {"Listed": False,
                           "Reason": f"Internal error occured - {error}"}
                    return (jsonify(jfy))


        @app.route('/api/v1/vip/<username>', methods=['GET'])
        def getusrplc(username):
            session = requests.session()
            account = open("Cookiecu.txt", "r").read()
            cookielogin = requests.cookies.RequestsCookieJar()
            cookielogin.set('.ROBLOSECURITY', account)
            session.cookies = cookielogin
            print("Getting user games...")

            uid1 = requests.get(f'https://api.roblox.com/users/get-by-username?username={username}').text
            json_data = json.loads(uid1)
            u_id = str(json_data["Id"])
            print(f".. Grabbed ID {u_id} ..")
            gameslist = json.loads(session.get(
                f"https://games.roblox.com/v2/users/{u_id}/games?accessFilter=Public&sortOrder=Asc&limit=10").text)
            unvid = gameslist["data"][0]["rootPlace"]["id"]

            url = "https://www.roblox.com/places/" + str(unvid) + "/update"
            return (jsonify({"Link": str(url)}))


        # add bal
        @app.route(f'/api/v1/admin/addbal/<user>/<amount>/<key>', methods=['GET'])
        def addbalapi(key, amount, user):
            # bcfe75f54587f53

            if key == "8a29dd59af2f8af":
                print(f"Authenticated action, adding {amount} to {user}")
                e1 = float(open(f"Database\\Pays\\{user}", "r").read())
                e1 += float(amount)
                # write to file
                e = open(f"Database\\Pays\\{user}", "w")
                e.write(str(e1))
                e.close()

                e = open(f"Database\\History\\{user}", "a")
                e.write(
                    f"A Developer added R${amount} to your balance | Added on {datetime.datetime.today().strftime('%Y-%m-%d')}\n")
                e.close()

                e = open(f"Database\\Moderator\\KRB", "a")
                e.write(f"[ + MODERATOR ] - Added {amount} to {user} .")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== Krabby has added {amount} to {user} == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')} ")
                e.close()
                return (jsonify({"Success": True,
                                 "Reason": f"[KRB] -> Added {amount} to {user}"}))

            elif key == "dcfe75f52f8a4587f56d9":
                print(f"Authenticated action, adding {amount} to {user}")
                e1 = float(open(f"Database\\Pays\\{user}", "r").read())
                e1 += float(amount)
                # write to file
                e = open(f"Database\\Pays\\{user}", "w")
                e.write(str(e1))
                e.close()

                e = open(f"Database\\History\\{user}", "a")
                e.write(
                    f"A Developer added R${amount} to your balance | Added on {datetime.datetime.today().strftime('%Y-%m-%d')}\n")
                e.close()

                e = open(f"Database\\Moderator\\OPM", "a")
                e.write(f"[ + MODERATOR ] - Added {amount} to {user} .")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== OPM has added {amount} to {user} == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')} ")
                e.close()
                return (jsonify({"Success": True,
                                 "Reason": f"[OPM] -> Added {amount} to {user}"}))

            elif key == "bcfe75f54587f53":
                print(f"Authenticated action, adding {amount} to {user}")
                e1 = float(open(f"Database\\Pays\\{user}", "r").read())
                e1 += float(amount)
                # write to file
                e = open(f"Database\\Pays\\{user}", "w")
                e.write(str(e1))
                e.close()

                e = open(f"Database\\History\\{user}", "a")
                e.write(
                    f"An Admin added R${amount} to your balance | Added on {datetime.datetime.today().strftime('%Y-%m-%d')}\n")
                e.close()

                e = open(f"Database\\Moderator\\CRSDE", "a")
                e.write(f"[ + MODERATOR ] - Added {amount} to {user} .")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== CRSDE has added {amount} to {user} == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')} ")
                e.close()
                return (jsonify({"Success": True,
                                 "Reason": f"[CRSDE] -> Added {amount} to {user}"}))


        @app.route(f'/api/v1/referral/signup/<org>/<user>', methods=['GET'])
        def refsignup(org, user):
            try:
                e = open(f"Database\\Pays\\{user}", "r").read()
                return ({"Success": False,
                         "Reason": "User already registered"})
            except:
                pass
            # Make sure we hide the reason to why it failed to make it harder for people to find a vulnerability - thus only returning if it was a success or not

            # first of all check if the owner has even checked stats to stop proxy vulnerability
            try:
                e = open(f"Database\\DIP\\{org}", "r").read()
            except Exception:
                print("Deal cannot be done due to refferral owner's ip never logged.")
                return ({"Success": False})

            refip = request.remote_addr

            # Check if in logged IPS
            e = open(f"Database\\FIPS\\dnd.txt", "r").readlines()
            for ips in e:
                if refip == ips:
                    print("IP has already been used, cannot do.")
                    return ({"Success": False})

            orginviter = org
            usr = user
            id = orginviter

            e = open(f"Database\\Ref\\E\\{orginviter}", "w")
            e.write("0")
            e.close()

            print(f"Registering user {user} under referral id {id}")

            print("== Performing security checks ==")

            print("== Checking if user has already registered ==")
            try:
                e = open(f"Database\\Pays\\{user}", "r").read()
            except Exception:
                print("== User isnt registered, continue to next security check ==")
                print("- Checking if referral is on same IP")
                orgip = open(f"Database\\DIP\\{id}", "r").read()
                if refip == orgip:
                    print(f"== Same IP has been detected | Reward FALSE")
                    return ({"Success": False,
                             "Reason": "IP has already been registered"})
                else:

                    print("Bypassed Major security checks | Performing roblox-checks...")
                    # Checking if user has previously registered on ACCO
                    try:
                        e = open(f"Database\\ACU\\{usr}", "r").read()
                    except Exception:
                        print("== Non-ACCO user ==")
                        print("... Grabbing ID...")
                        uid1 = requests.get(f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        u_id = json_data["Id"]
                        print(f".. Grabbed ID {u_id} ..")
                        print(".. Grabbing Headshot ..")
                        try:
                            headshotjson = json.loads(requests.get(
                                f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={u_id}&size=150x150&format=Png&isCircular=true").text)
                            headshot = headshotjson["data"][0]["imageUrl"]
                            print(f".. Grabbed Headshot {headshot} ..")
                        except Exception as e:
                            print(f"Error getting headshot for {usr} | {e}")
                            headshot = f"http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username={usr}"

                        e = open(f"Database\\Headshots\\{usr}", "w")
                        e.write(headshot)
                        e.close()

                        e = open(f"Database\\DOffer\\{usr}", "w")
                        e.write("0")
                        e.close()

                        writepay = open("Database\\Pays\\" + usr, 'w')
                        writepay.write("0")
                        writepay.close()
                        inforet = 'Valid*True*Registered'
                        print("registered")

                        e = open(f"Database\\DIP\\{usr}", "w")
                        e.write(str(request.remote_addr))
                        e.close()

                        e = open(f"Database\\Ref\\E\\{orginviter}", "w")
                        e.write("0")
                        e.close()

                        dte = str(datetime.datetime.today().strftime('%Y-%m-%d'))

                        e = open(f"Database\\History\\{user}", "w")
                        e.write(
                            f"Successfully registered account on {dte} - Welcome to CoolBux, the site to get free Robux!\n")
                        e.close()

                        crnt = int(open(f"Database\\Ref\\T\\{orginviter}", "r").read())
                        crnt += 1
                        tmr = open(f"Database\\Ref\\T\\{orginviter}", "w")
                        dafsafsd = str(crnt)
                        tmr.write(dafsafsd)
                        tmr.close()

                        # Append to logged IPS

                        e = open(f"Database\\FIPS\\dnd.txt", "a")
                        e.write("\n" + str(request.remote_addr))
                        e.close()

                        # Append to referrer
                        apef = open(f"Database\\Ref\\W\\{usr}", "w")
                        apef.write(orginviter)
                        apef.close()

                        info = {"Registered": True,
                                "Reason": "Registered",
                                "PreACCO": False}
                        return (jsonify(info))
                    else:
                        print("== ACCO User! Registering account and adding bonus! ==")

                        print("... Grabbing ID...")
                        uid1 = requests.get(f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        u_id = json_data["Id"]
                        print(f".. Grabbed ID {u_id} ..")
                        print(".. Grabbing Headshot ..")
                        try:
                            headshotjson = json.loads(requests.get(
                                f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={u_id}&size=150x150&format=Png&isCircular=true").text)
                            headshot = headshotjson["data"][0]["imageUrl"]
                            print(f".. Grabbed Headshot {headshot} ..")
                        except Exception as e:
                            print(f"Error getting headshot for {usr} | {e}")
                            headshot = f"http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username={usr}"

                        e = open(f"Database\\Headshots\\{usr}", "w")
                        e.write(headshot)
                        e.close()

                        # Get previous balance of them in acco
                        preac = int(float(open(f"Database\\ACU\\{usr}").read())) / 39

                        if preac < 1:
                            preac = 0.25

                        if preac > 85:
                            preac = 85

                        writepay = open("Database\\Pays\\" + usr, 'w')
                        writepay.write(str(preac))
                        writepay.close()
                        inforet = 'Valid*True*Registered'
                        print("registered")

                        e = open(f"Database\\DIP\\{usr}", "w")
                        e.write(str(request.remote_addr))
                        e.close()

                        dte = str(datetime.datetime.today().strftime('%Y-%m-%d'))

                        e = open(f"Database\\History\\{user}", "w")
                        e.write(
                            f"Successfully registered account on {dte} - Welcome to CoolBux, the site to get free Robux!\nReceived Welcome Gift of R${preac}\n")
                        e.close()

                        e = open(f"Database\\DOffer\\{usr}", "w")
                        e.write("0")
                        e.close()

                        crnt = int(open(f"Database\\Ref\\T\\{orginviter}", "r").read())
                        crnt += 1
                        tmr = open(f"Database\\Ref\\T\\{orginviter}", "w")
                        dafsafsd = str(crnt)
                        tmr.write(dafsafsd)
                        tmr.close()

                        # Append to logged IPS

                        e = open(f"Database\\FIPS\\dnd.txt", "a")
                        e.write("\n" + str(request.remote_addr))
                        e.close()

                        # Append to referrer
                        apef = open(f"Database\\Ref\\W\\{usr}", "w")
                        apef.write(orginviter)
                        apef.close()
                        info = {"Registered": True,
                                "Reason": "Registered",
                                "PreACCO": True,
                                "Bonus": str(int(float(preac)))}
                        return (jsonify(info))


        # ban note
        @app.route('/api/v1/banned/note/<user>', methods=['GET'])
        def bannote(user):
            return (open(f"Database\\Banned\\{user}", "r").read())


        @limiter.limit("60 per minute")
        @app.route('/api/v2/captcha/<token>/<username>', methods=['GET'])
        def captchachecksv2(token, username):

            if True == True:
                if request.headers.get('ext'):
                    host = 'localhost'  # Host Name
                    port = 6969  # Port Number
                    s = socket.socket()  # Create Socket
                    s.connect((host, port))  # Connect to socket
                    print("Socket Is Connected....")
                    msgsend = jpysocket.jpyencode(f"{token}:{username}:1")
                    s.send(msgsend)  # Send Msg
                    msgrecv = s.recv(1024)  # Recieve msg
                    lmf = '{"' + jpysocket.jpydecode(msgrecv)  # Decript msg
                    print(lmf)
                    s.close()  # Close connection
                    # -send msg
                    fld = json.loads(lmf)["Failed"]
                    # Get user information
                    uid1 = requests.get(
                        f'https://api.roblox.com/users/get-by-username?username={username}').text
                    json_data = json.loads(uid1)
                    ud2 = json_data["Id"]
                    u_id = str(ud2)
                    print(f".. Grabbed ID {u_id} ..")
                    iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                    if fld == "True":

                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{username}** Just solved a captcha!",
                                        "description": f"**{username}** Just solved a captcha and earned **ROBUX!**",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{username}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {username} just did! | Extention enabled"
                                        }
                                    }
                                ]
                            })
                    else:
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{username}** Just failed to solve a captcha!",
                                        "description": f"**{username}** Failed to solve a captcha and missed out on **robux**",
                                        "color": 16597570,
                                        "author": {
                                            "name": f"{username}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                        }
                                    }
                                ]
                            })
                    return jsonify((lmf))
                else:
                    host = 'localhost'  # Host Name
                    port = 6969  # Port Number
                    s = socket.socket()  # Create Socket
                    s.connect((host, port))  # Connect to socket
                    print("Socket Is Connected....")
                    msgsend = jpysocket.jpyencode(f"{token}:{username}:0")
                    s.send(msgsend)  # Send Msg
                    msgrecv = s.recv(1024)  # Recieve msg
                    lmf = '{"' + jpysocket.jpydecode(msgrecv)  # Decript msg
                    s.close()  # Close connection
                    # -send msg
                    print(lmf)
                    fld = json.loads(lmf)["Failed"]
                    # Get user information
                    uid1 = requests.get(
                        f'https://api.roblox.com/users/get-by-username?username={username}').text
                    json_data = json.loads(uid1)
                    ud2 = json_data["Id"]
                    u_id = str(ud2)
                    print(f".. Grabbed ID {u_id} ..")
                    iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                    if fld == "True":

                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{username}** Just solved a captcha!",
                                        "description": f"**{username}** Just solved a captcha and earned **ROBUX!**",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{username}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {username} just did!"
                                        }
                                    }
                                ]
                            })
                    else:
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{username}** Just failed to solve a captcha!",
                                        "description": f"**{username}** Failed to solve a captcha and missed out on **robux**",
                                        "color": 16597570,
                                        "author": {
                                            "name": f"{username}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                        }
                                    }
                                ]
                            })
                    return jsonify((lmf))

            if request.headers.get('ext'):
                print("extension has been activated")
                usr = username
                ID = token
                if True == True:
                    password = str(random.randrange(0, 9999999999999999))
                    global tries

                    def Vuser():
                        for n in range(10):
                            info = str(requests.get(
                                f"https://users.roblox.com/v1/users/{random.randrange(0, 90000000)}").text)
                            try:
                                print(info)
                                username2 = json.loads(info)['name'] + str(random.randrange(0, 9999))
                                print(f"Gen user  | {username2}")
                            except Exception as e:
                                print("USR GEN ERROR: " + str(e))
                                pass
                            gtoken = requests.post("https://auth.roblox.com/v1/usernames/validate",
                                                   {"birthday": "1998-03-02T13:00:00.000Z", "context": "Signup",
                                                    "username": "s3df345"}).headers['X-CSRF-TOKEN']
                            validate = requests.post("https://auth.roblox.com/v1/usernames/validate",
                                                     {"birthday": "1998-03-02T13:00:00.000Z",
                                                      "context": "Signup", "username": username2},
                                                     headers={"x-csrf-token": gtoken}).text
                            print(f"Validating {username2}")
                            if validate == '{"code":0,"message":"Username is valid"}':
                                print("Valid username")
                                return (username2)
                            else:
                                print(f"Failed validate {validate}")
                                pass

                    try:
                        username = Vuser()
                    except Exception:
                        username = str(requests.get("https://blacktippen.pythonanywhere.com/genuser").text)

                    def Create(token, username):

                        proxycoice = random.choice(proxylistprivate).strip('\n')
                        print('chose proxy', proxycoice, ' v2')
                        # create the request to get the xsrf token
                        xsr = requests.post("https://auth.roblox.com/v2/signup",
                                            data={"username": "q4w5tsgfd", "password": "sdgfsdfg",
                                                  "birthday": "05 Jun 2005",
                                                  "gender": 2, "isTosAgreementBoxChecked": True,
                                                  "context": "MultiverseSignupForm", "referralData": None,
                                                  "displayAvatarV2": False, "displayContextV2": False,
                                                  "captchaToken": None,
                                                  "captchaProvider": "PROVIDER_ARKOSE_LABS"},
                                            proxies={"https": proxycoice}).headers['X-CSRF-TOKEN']
                        # create the real request here
                        signup = requests.post("https://auth.roblox.com/v2/signup",
                                               data={"username": username, "password": password,
                                                     "birthday": "07 Jun 2005",
                                                     "gender": 2, "isTosAgreementBoxChecked": True,
                                                     "context": "MultiverseSignupForm", "referralData": None,
                                                     "displayAvatarV2": False, "displayContextV2": False,
                                                     "captchaToken": token,
                                                     "captchaProvider": "PROVIDER_ARKOSE_LABS"},
                                               headers={"X-CSRF-TOKEN": xsr}, proxies={"https": proxycoice})
                        print(f"vignup: " + str(signup.text))
                        cookie = str(signup.cookies['.ROBLOSECURITY'])
                        # check if we created the account
                        try:
                            parsed = json.loads(signup.text)["userId"]
                        except Exception:
                            return ({
                                        "Done": False,
                                        "Status": f"Failed",
                                        "Reward": 1,
                                        "Failed": True,
                                        "Warn": False,
                                        "TotalCaptchas": "Failed"
                                    }, 200, {'isCorrect': False})
                        else:
                            print(f"Created userID {parsed} | Username {username}")
                            formatsave = str(f"{username}:{password}:{cookie}\n")
                            print(f"Save: {formatsave}")
                            with open("Cookies\\cookiesbatch2.txt", "a") as f:
                                f.write(formatsave)
                                f.flush()
                                print(f"Saved account '{username}' ")
                                return ("Created")

                    fc_token2323 = str(
                        token) + "|r=ap-southeast-1|metabgclr=transparent|guitextcolor=%23474747|maintxtclr=%23b8b8b8|metaiconclr=transparent|meta=6|lang=en|pk=A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F|at=40|rid=50|ht=1|atp=2|cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-ap-southeast-1.arkoselabs.com|surl=https%3A%2F%2Froblox-api.arkoselabs.com"
                    try:
                        created = Create(fc_token2323, username)
                        # unlock signup with fc-token
                    except Exception as e:
                        print(f"{e} | Failed to create account | Bad token (Exception)")
                        n = 'False'
                        info = "F"
                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just failed to solve a captcha!",
                                        "description": f"**{usr}** Failed to solve a captcha and missed out on **robux**",
                                        "color": 16597570,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                        }
                                    }
                                ]
                            })
                        return ({
                                    "Done": False,
                                    "Status": f"Failed",
                                    "Reward": 1,
                                    "Failed": True,
                                    "Warn": False,
                                    "TotalCaptchas": "Failed"
                                }, 200, {'isCorrect': False})

                    if created == "Created":
                        print(f"Account '{username}' has been created , awarding creator")
                        dreward = 0.12

                        print("-- adding balance --")
                        # get current balance
                        cbal22 = open('Database\\Pays\\' + usr, 'r')
                        cbal2 = cbal22.read()
                        cbal22.close()
                        cbal = float(cbal2)
                        print(cbal)
                        # add their balance
                        cbal += dreward
                        nbal = str(cbal)
                        print(nbal)
                        # apply their balance
                        add = open('Database\\Pays\\' + usr, 'w')
                        add.write(nbal)
                        add.close()
                        print(f"-- Added balance to {usr} --")

                        info = {"Solved": True,
                                "Reason": "Funcaptcha has been solved",
                                "Time": "0"}

                        # wait for account to setup

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"

                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just solved a captcha!",
                                        "description": f"**{usr}** Just solved a captcha and earned **ROBUX!**",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did! | Extention enabled"
                                        }
                                    }
                                ]
                            })

                        print("== Checking captcha status on user ==")
                        try:
                            crntcaptchas = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[0])
                        except Exception:
                            crntcaptchas = 1
                            e = open(f"Database\\Captchas\\{usr}", "w")
                            e.write("1*1")
                            e.close()
                            return ({
                                        "Done": True,
                                        "Status": f"1/8",
                                        "Reward": 1,
                                        "Failed": False,
                                        "Warn": False,
                                        "TotalCaptchas": 1
                                    }, 200, {'isCorrect': True})
                        else:
                            crntcaptchas += 1
                            if crntcaptchas == 8:
                                print(f"== Reset captchas on {usr}")
                                solvedatm = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[1])
                                newatm = solvedatm + 1
                                e = open(f"Database\\Captchas\\{usr}", "w")
                                e.write(f"0*{str(newatm)}")
                                e.close()
                                e = open(f"Database\\History\\{usr}", "a")
                                e.write(
                                    f"Rewarded R$1 For solving 8 captchas.\n")
                                e.close()
                                return ({
                                            "Done": True,
                                            "Status": f"8/8",
                                            "Reward": 1,
                                            "Failed": False,
                                            "Warn": False,
                                            "TotalCaptchas": str(solvedatm)
                                        }, 200, {'isCorrect': True})
                            else:
                                totalsolved = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[0])
                                solvedatm = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[1])
                                newttsolved = totalsolved + 1
                                newatm = solvedatm + 1
                                e = open(f"Database\\Captchas\\{usr}", "w")
                                e.write(f"{str(newttsolved)}*{str(newatm)}")
                                e.close()
                                return ({
                                            "Done": True,
                                            "Status": f"{str(crntcaptchas)}/8",
                                            "Reward": 1,
                                            "Failed": False,
                                            "Warn": False,
                                            "TotalCaptchas": str(solvedatm)
                                        }, 200, {'isCorrect': True})
                    else:
                        print(created)

                        # Get user information
                        uid1 = requests.get(
                            f'https://api.roblox.com/users/get-by-username?username={usr}').text
                        json_data = json.loads(uid1)
                        ud2 = json_data["Id"]
                        u_id = str(ud2)
                        print(f".. Grabbed ID {u_id} ..")
                        iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just failed to solve a captcha!",
                                        "description": f"**{usr}** Failed to solve a captcha and missed out on **robux**",
                                        "color": 16597570,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                        }
                                    }
                                ]
                            })
                        return ({
                                    "Done": False,
                                    "Status": f"Failed",
                                    "Reward": 1,
                                    "Failed": True,
                                    "TotalCaptchas": "Failed"
                                }, 200, {'isCorrect': False})

            print("traditional award system activated")
            usr = username
            ID = token
            if True == True:
                password = str(random.randrange(0, 9999999999999999))
                global tries

                def Vuser():
                    for n in range(10):
                        info = str(requests.get(
                            f"https://users.roblox.com/v1/users/{random.randrange(0, 90000000)}").text)
                        try:
                            print(info)
                            username2 = json.loads(info)['name'] + str(random.randrange(0, 9999))
                            print(f"Gen user  | {username2}")
                        except Exception as e:
                            print("USR GEN ERROR: " + str(e))
                            pass
                        gtoken = requests.post("https://auth.roblox.com/v1/usernames/validate",
                                               {"birthday": "1998-03-02T13:00:00.000Z", "context": "Signup",
                                                "username": "s3df345"}).headers['X-CSRF-TOKEN']
                        validate = requests.post("https://auth.roblox.com/v1/usernames/validate",
                                                 {"birthday": "1998-03-02T13:00:00.000Z",
                                                  "context": "Signup", "username": username2},
                                                 headers={"x-csrf-token": gtoken}).text
                        print(f"Validating {username2}")
                        if validate == '{"code":0,"message":"Username is valid"}':
                            print("Valid username")
                            return (username2)
                        else:
                            print(f"Failed validate {validate}")
                            pass

                try:
                    username = Vuser()
                except Exception:
                    username = str(requests.get("https://blacktippen.pythonanywhere.com/genuser").text)

                def Create(token, username):

                    proxycoice = random.choice(proxylistprivate).strip('\n')
                    print('chose proxy', proxycoice, ' v2')
                    # create the request to get the xsrf token
                    xsr = requests.post("https://auth.roblox.com/v2/signup",
                                        data={"username": "q4w5tsgfd", "password": "sdgfsdfg",
                                              "birthday": "05 Jun 2005",
                                              "gender": 2, "isTosAgreementBoxChecked": True,
                                              "context": "MultiverseSignupForm", "referralData": None,
                                              "displayAvatarV2": False, "displayContextV2": False,
                                              "captchaToken": None,
                                              "captchaProvider": "PROVIDER_ARKOSE_LABS"},
                                        proxies={"https": proxycoice}).headers['X-CSRF-TOKEN']
                    # create the real request here
                    signup = requests.post("https://auth.roblox.com/v2/signup",
                                           data={"username": username, "password": password,
                                                 "birthday": "07 Jun 2005",
                                                 "gender": 2, "isTosAgreementBoxChecked": True,
                                                 "context": "MultiverseSignupForm", "referralData": None,
                                                 "displayAvatarV2": False, "displayContextV2": False,
                                                 "captchaToken": token,
                                                 "captchaProvider": "PROVIDER_ARKOSE_LABS"},
                                           headers={"X-CSRF-TOKEN": xsr}, proxies={"https": proxycoice})
                    print(f"vignup: " + str(signup.text))
                    cookie = str(signup.cookies['.ROBLOSECURITY'])
                    # check if we created the account
                    try:
                        parsed = json.loads(signup.text)["userId"]
                    except Exception:
                        return ({
                            "Done": False,
                            "Status": f"Failed",
                            "Reward": 1,
                            "Failed": True,
                            "Warn": False,
                            "TotalCaptchas": "Failed"
                        })
                    else:
                        print(f"Created userID {parsed} | Username {username}")
                        formatsave = str(f"{username}:{password}:{cookie}\n")
                        print(f"Save: {formatsave}")
                        with open("Cookies\\cookiesbatch2.txt", "a") as f:
                            f.write(formatsave)
                            f.flush()
                            print(f"Saved account '{username}' ")
                            return ("Created")

                fc_token2323 = str(
                    token) + "|r=ap-southeast-1|metabgclr=transparent|guitextcolor=%23474747|maintxtclr=%23b8b8b8|metaiconclr=transparent|meta=6|lang=en|pk=A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F|at=40|rid=50|ht=1|atp=2|cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-ap-southeast-1.arkoselabs.com|surl=https%3A%2F%2Froblox-api.arkoselabs.com"
                try:
                    created = Create(fc_token2323, username)
                    # unlock signup with fc-token
                except Exception as e:
                    print(f"{e} | Failed to create account | Bad token (Exception)")
                    n = 'False'
                    info = "F"
                    # Get user information
                    uid1 = requests.get(
                        f'https://api.roblox.com/users/get-by-username?username={usr}').text
                    json_data = json.loads(uid1)
                    ud2 = json_data["Id"]
                    u_id = str(ud2)
                    print(f".. Grabbed ID {u_id} ..")
                    iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                        json={
                            "embeds": [
                                {
                                    "title": f"**{usr}** Just failed to solve a captcha!",
                                    "description": f"**{usr}** Failed to solve a captcha and missed out on **robux**",
                                    "color": 16597570,
                                    "author": {
                                        "name": f"{usr}",
                                        "icon_url": iconauth
                                    },
                                    "footer": {
                                        "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                    }
                                }
                            ]
                        })
                    return ({
                                "Done": False,
                                "Status": f"Failed",
                                "Reward": 1,
                                "Failed": True,
                                "Warn": False,
                                "TotalCaptchas": "Failed"
                            }, 200, {'isCorrect': True})

                if created == "Created":
                    print(f"Account '{username}' has been created , awarding creator")

                    # --calculate reward

                    dreward = 0.1
                    print("-- adding balance --")
                    # get current balance
                    cbal22 = open('Database\\Pays\\' + usr, 'r')
                    cbal2 = cbal22.read()
                    cbal22.close()
                    cbal = float(cbal2)
                    print(cbal)
                    # add their balance
                    cbal += dreward
                    nbal = str(cbal)
                    print(nbal)
                    # apply their balance
                    add = open('Database\\Pays\\' + usr, 'w')
                    add.write(nbal)
                    add.close()
                    print(f"-- Added balance to {usr} --")

                    info = {"Solved": True,
                            "Reason": "Funcaptcha has been solved",
                            "Time": "0"}

                    # wait for account to setup

                    # Get user information
                    uid1 = requests.get(
                        f'https://api.roblox.com/users/get-by-username?username={usr}').text
                    json_data = json.loads(uid1)
                    ud2 = json_data["Id"]
                    u_id = str(ud2)
                    print(f".. Grabbed ID {u_id} ..")
                    iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"

                    requests.post(
                        "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                        json={
                            "embeds": [
                                {
                                    "title": f"**{usr}** Just solved a captcha!",
                                    "description": f"**{usr}** Just solved a captcha and earned **R${dreward}**",
                                    "color": 8519030,
                                    "author": {
                                        "name": f"{usr}",
                                        "icon_url": iconauth
                                    },
                                    "footer": {
                                        "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                    }
                                }
                            ]
                        })

                    print("== Checking captcha status on user ==")
                    try:
                        crntcaptchas = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[0])
                    except Exception:
                        crntcaptchas = 1
                        e = open(f"Database\\Captchas\\{usr}", "w")
                        e.write("1*1")
                        e.close()
                        return ({
                                    "Done": True,
                                    "Status": f"1/8",
                                    "Reward": 1,
                                    "Failed": False,
                                    "Warn": False,
                                    "TotalCaptchas": 1
                                }, 200, {'isCorrect': True})
                    else:
                        crntcaptchas += 1
                        if crntcaptchas == 8:
                            print(f"== Reset captchas on {usr}")
                            solvedatm = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[1])
                            newatm = solvedatm + 1
                            e = open(f"Database\\Captchas\\{usr}", "w")
                            e.write(f"0*{str(newatm)}")
                            e.close()
                            e = open(f"Database\\History\\{usr}", "a")
                            e.write(
                                f"Rewarded R$1 For solving 8 captchas.\n")
                            e.close()
                            return ({
                                        "Done": True,
                                        "Status": f"8/8",
                                        "Reward": 1,
                                        "Failed": False,
                                        "Warn": False,
                                        "TotalCaptchas": str(solvedatm)
                                    }, 200, {'isCorrect': True})
                        else:
                            totalsolved = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[0])
                            solvedatm = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[1])
                            newttsolved = totalsolved + 1
                            newatm = solvedatm + 1
                            e = open(f"Database\\Captchas\\{usr}", "w")
                            e.write(f"{str(newttsolved)}*{str(newatm)}")
                            e.close()
                            return ({
                                        "Done": True,
                                        "Status": f"{str(crntcaptchas)}/8",
                                        "Reward": 1,
                                        "Failed": False,
                                        "Warn": False,
                                        "TotalCaptchas": str(solvedatm)
                                    }, 200, {'isCorrect': True})
                else:
                    print(created)

                    # Get user information
                    uid1 = requests.get(
                        f'https://api.roblox.com/users/get-by-username?username={usr}').text
                    json_data = json.loads(uid1)
                    ud2 = json_data["Id"]
                    u_id = str(ud2)
                    print(f".. Grabbed ID {u_id} ..")
                    iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                        json={
                            "embeds": [
                                {
                                    "title": f"**{usr}** Just failed to solve a captcha!",
                                    "description": f"**{usr}** Failed to solve a captcha and missed out on **robux**",
                                    "color": 16597570,
                                    "author": {
                                        "name": f"{usr}",
                                        "icon_url": iconauth
                                    },
                                    "footer": {
                                        "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                    }
                                }
                            ]
                        })
                    return ({
                        "Done": False,
                        "Status": f"Failed",
                        "Reward": 1,
                        "Failed": True,
                        "TotalCaptchas": "Failed"
                    })


        @app.route('/api/v1/captcha/<token>/<username>/<ptype>', methods=['GET'])
        def captchachecks(token, username, ptype):
            ID = token
            usr = username
            print(f"Testing if user {usr} exists...")
            try:
                e = open('Database\\Pays\\' + str(usr), 'r')
                e.read()
                e.close()
            except Exception:
                info = {"Solved": False,
                        "Reason": "No Account",
                        "Time": "0"}
                return (info)
            else:
                # Get user information
                uid1 = requests.get(
                    f'https://api.roblox.com/users/get-by-username?username={usr}').text
                json_data = json.loads(uid1)
                ud2 = json_data["Id"]
                u_id = str(ud2)
                print(f".. Grabbed ID {u_id} ..")
                iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"

                # validate captcha here

                vtoken = requests.post("https://roblox-api.arkoselabs.com/fc/gfct/",
                                       {"token": token, "sid": "ap-southeast-1", "render_type": "canvas",
                                        "data[status]": "init", "analytics_tier": 40, "lang": "en"})
                capresp = json.loads(vtoken.text)
                if capresp["challengeURL"] == '001':
                    print("invalid captcha")
                    # appending to score (if exceeds 25 invalid within an hour we temporarily ban for )
                    try:
                        score = open(f"Database\\Captcha\\Score\\{usr}", "r").read()
                    except Exception:
                        # create them a score
                        e = open(f"Database\\Captcha\\Score\\{usr}", "w")
                        e.write(f"1*{time.time()}")
                        e.close()
                    else:
                        print("Checking score (program auto resets at 1 hour)")
                        if float(score) > 24:
                            print("ban user temporarily for 1 hour")
                            e = open(f"Database\\Captcha\\TBan\\{usr}", "w")
                            e.write(
                                f"You currently cannot create captchas for an hour due to you submitting too many invalid captchas. Please don't submit invalid captchas, if you can't solve it hit the refresh button, otherwise you can't do captchas for an hour.*{time.time()}")
                            e.close()
                            requests.post(
                                "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                                json={
                                    "embeds": [
                                        {
                                            "title": f"**{usr}** Got Captcha Banned!",
                                            "description": f"**{usr}** Has got banned temporarily for an hour on captchas due to submitting too many invalid captchas.",
                                            "color": 16597570,
                                            "author": {
                                                "name": f"{usr}",
                                                "icon_url": iconauth
                                            },
                                            "footer": {
                                                "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                            }
                                        }
                                    ]
                                })
                            info = {"Solved": False,
                                    "Reason": "Captcha Banned"}
                            return (info)
                        else:
                            print("append to score")
                            score += 1
                            e = open(f"Database\\Captcha\\Score\\{usr}", "w")
                            e.write(str(score))
                            e.close()
                            requests.post(
                                "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                                json={
                                    "embeds": [
                                        {
                                            "title": f"**{usr}** Just failed to solve a captcha!",
                                            "description": f"**{usr}** Failed to solve a captcha and missed out on **robux**",
                                            "color": 16597570,
                                            "author": {
                                                "name": f"{usr}",
                                                "icon_url": iconauth
                                            },
                                            "footer": {
                                                "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                            }
                                        }
                                    ]
                                })
                            info = {"Solved": False,
                                    "Reason": "Invalid captcha",
                                    "Warned": True,
                                    "Warning": "Don't submit invalid captchas, if you keep doing this you will be banned temporarily."}
                            return (info)

                else:
                    print("check captcha difficulty")  # based on waves in captcha
                    capwaves = int(capresp["waves"])
                    # calculate reward
                    maxreward = 0.125
                    dreward = 0.10

                    def CalculateReward(waves, maxreward):
                        if int(waves) == 1:
                            dreward = 0.10
                        elif int(waves) == 2:
                            dreward = 0.105
                        elif int(waves) == 3:
                            dreward = 0.11
                        elif int(waves) == 4:
                            dreward = 0.12
                        else:
                            dreward = maxreward

                    # check if any users are in queue
                    count = 0
                    for nln in open("Database\\Captcha\\queue.bin", "r").read().split("\n"):
                        if nln == "\n":
                            pass
                        else:
                            count += 1
                    if count > 0:
                        print(f"{count} users in queue")
                        # give to highest priority in queue (if anyone is paying over 0.0009)
                        nbid = 0.0009
                        tskid = None
                        ogapikey = None
                        for nln in open("Database\\Captcha\\queue.bin", "r").read().split("\n"):
                            if float(nln.split("*")[1]) > nbid:
                                if ptype == nln.split("*")[3]:
                                    nbid = float(nln.split("*")[1])
                                    tskid = nln.split("*")[0]
                                    ogapikey = nln.split("*")[2]
                                else:
                                    pass
                            else:
                                pass
                        if tskid == None & nbid == 0.0009:
                            print("No priority bidders found, using longest awaiting bidder")
                            with open('Database\\Captcha\\queue.bin', 'r') as f:
                                lines = f.read().splitlines()
                                awbidder = lines[-1]
                                tskid = awbidder.split("*")[0]
                                ogapikey = awbidder.split("*")[2]

                        # task finish system here
                        print(f"Rewarding captcha to {tskid} ")
                        e = open(f"Database\\Captcha\\Completed\\{tskid}", "w")
                        e.write(f"{token}*{usr}*{nbid}*{time.time()}")
                        e.close()

                        # remove from pending captchas
                        cepnd = int(open(f"Database\\Captcha\\CEpnd\\{ogapikey}", "r").read())
                        cepnd -= 1
                        newpend = open(f"Database\\Captcha\\CEpnd\\{ogapikey}", "r")
                        newpend.write(str(cepnd))
                        newpend.close()

                        nbal = int(open(f"Database\\Captcha\\TotalSolved\\{ogapikey}", "r").read()) + 1
                        e = open(f"Database\\Captcha\\TotalSolved\\{ogapikey}", "w")
                        e.write(str(nbal))
                        e.close()

                        # add to logs
                        print("adding to logs")
                        e = open(f"Database\\Logs\\ApiKeys\\{ogapikey}", "a")
                        e.write(
                            f"tskid: {tskid} cost:{str(nbid)} creator: {usr} token: {token} qsize: {str(count)} | usrwd: {dreward} | type {ptype}")
                        e.close()

                        # now put the robux in coolbux-pending (program checks all & rewards)
                        try:
                            cbd = float(open(f"Database\\Captchas\\Pending\\{usr}", "r").read())
                        except Exception:
                            e = open(f"Database\\Captchas\\Pending\\{usr}", "w")
                            e.write(f"{dreward}")
                            e.close()
                            # create individual transaction
                            transactionid = str(secrets.token_hex(12))
                            e = open(f"Database\\Captchas\\Pending\\TXDS\\{transactionid}", "w")
                            e.write(f"{dreward}*{time.time()}")
                            e.close()

                        else:
                            # add reward here
                            cbd += dreward
                            e = open(f"Database\\Captchas\\Pending\\{usr}", "w")
                            e.write(str(cbd))
                            e.close()

                        requests.post(
                            "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                            json={
                                "embeds": [
                                    {
                                        "title": f"**{usr}** Just solved a captcha!",
                                        "description": f"**{usr}** Just solved a captcha and earned **R${dreward}**",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{usr}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                        }
                                    }
                                ]
                            })
                        try:
                            crntcaptchas = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[0])
                        except Exception:
                            crntcaptchas = 1
                            e = open(f"Database\\Captchas\\{usr}", "w")
                            e.write("1*1")
                            e.close()
                            return ({
                                "Done": True,
                                "Status": f"1/8",
                                "Reward": 1,
                                "Failed": False,
                                "Warn": False,
                                "TotalCaptchas": 1
                            })
                        else:
                            crntcaptchas += 1
                            if crntcaptchas == 8:
                                print(f"== Reset captchas on {usr}")
                                solvedatm = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[1])
                                newatm = solvedatm + 1
                                e = open(f"Database\\Captchas\\{usr}", "w")
                                e.write(f"0*{str(newatm)}")
                                e.close()
                                e = open(f"Database\\History\\{usr}", "a")
                                e.write(
                                    f"Rewarded R$1 For solving 8 captchas.\n")
                                e.close()
                                return ({
                                    "Done": True,
                                    "Status": f"8/8",
                                    "Reward": 1,
                                    "Failed": False,
                                    "Warn": False,
                                    "TotalCaptchas": str(solvedatm)
                                })
                            else:
                                totalsolved = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[0])
                                solvedatm = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[1])
                                newttsolved = totalsolved + 1
                                newatm = solvedatm + 1
                                e = open(f"Database\\Captchas\\{usr}", "w")
                                e.write(f"{str(newttsolved)}*{str(newatm)}")
                                e.close()
                                return ({
                                    "Done": True,
                                    "Status": f"{str(crntcaptchas)}/8",
                                    "Reward": 1,
                                    "Failed": False,
                                    "Warn": False,
                                    "TotalCaptchas": str(solvedatm)
                                })
                    else:
                        print("traditional award system activated (no users in queue)")
                        if True == True:
                            password = str(random.randrange(0, 9999999999999999))
                            global tries

                            def Vuser():
                                for n in range(10):
                                    info = str(requests.get(
                                        f"https://users.roblox.com/v1/users/{random.randrange(0, 90000000)}").text)
                                    try:
                                        print(info)
                                        username2 = json.loads(info)['name'] + str(random.randrange(0, 9999))
                                        print(f"Gen user  | {username2}")
                                    except Exception as e:
                                        print("USR GEN ERROR: " + str(e))
                                        pass
                                    gtoken = requests.post("https://auth.roblox.com/v1/usernames/validate",
                                                           {"birthday": "1998-03-02T13:00:00.000Z", "context": "Signup",
                                                            "username": "s3df345"}).headers['X-CSRF-TOKEN']
                                    validate = requests.post("https://auth.roblox.com/v1/usernames/validate",
                                                             {"birthday": "1998-03-02T13:00:00.000Z",
                                                              "context": "Signup", "username": username2},
                                                             headers={"x-csrf-token": gtoken}).text
                                    print(f"Validating {username2}")
                                    if validate == '{"code":0,"message":"Username is valid"}':
                                        print("Valid username")
                                        return (username2)
                                    else:
                                        print(f"Failed validate {validate}")
                                        pass

                            try:
                                username = Vuser()
                            except Exception:
                                username = str(requests.get("https://blacktippen.pythonanywhere.com/genuser").text)

                            def Create(token, username):
                                # create the request to get the xsrf token
                                xsr = requests.post("https://auth.roblox.com/v2/signup",
                                                    data={"username": "q4w5tsgfd", "password": "sdgfsdfg",
                                                          "birthday": "05 Jun 2005",
                                                          "gender": 2, "isTosAgreementBoxChecked": True,
                                                          "context": "MultiverseSignupForm", "referralData": None,
                                                          "displayAvatarV2": False, "displayContextV2": False,
                                                          "captchaToken": None,
                                                          "captchaProvider": "PROVIDER_ARKOSE_LABS"}).headers[
                                    'X-CSRF-TOKEN']
                                # create the real request here
                                signup = requests.post("https://auth.roblox.com/v2/signup",
                                                       data={"username": username, "password": password,
                                                             "birthday": "07 Jun 2005",
                                                             "gender": 2, "isTosAgreementBoxChecked": True,
                                                             "context": "MultiverseSignupForm", "referralData": None,
                                                             "displayAvatarV2": False, "displayContextV2": False,
                                                             "captchaToken": token,
                                                             "captchaProvider": "PROVIDER_ARKOSE_LABS"},
                                                       headers={"X-CSRF-TOKEN": xsr})
                                print(signup.text)
                                cookie = str(signup.cookies['.ROBLOSECURITY'])
                                # check if we created the account
                                try:
                                    parsed = json.loads(signup.text)["userId"]
                                except Exception:
                                    return ({
                                        "Done": False,
                                        "Status": f"Failed",
                                        "Reward": 1,
                                        "Failed": True,
                                        "Warn": False,
                                        "TotalCaptchas": "Failed"
                                    })
                                else:
                                    print(f"Created userID {parsed} | Username {username}")
                                    formatsave = str(f"{username}:{password}:{cookie}\n")
                                    print(f"Save: {formatsave}")
                                    with open("unqueuecook.txt", "a") as f:
                                        f.write(formatsave)
                                        f.flush()
                                        print(f"Saved account '{username}' ")
                                        return ("Created")

                            fc_token2323 = str(
                                token) + "|r=ap-southeast-1|metabgclr=transparent|guitextcolor=%23474747|maintxtclr=%23b8b8b8|metaiconclr=transparent|meta=6|lang=en|pk=A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F|at=40|rid=50|ht=1|atp=2|cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-ap-southeast-1.arkoselabs.com|surl=https%3A%2F%2Froblox-api.arkoselabs.com"
                            try:
                                created = Create(fc_token2323, username)
                                # unlock signup with fc-token
                            except Exception:
                                print("Failed to create account | Bad token (Exception)")
                                n = 'False'
                                info = "F"
                                # Get user information
                                uid1 = requests.get(
                                    f'https://api.roblox.com/users/get-by-username?username={usr}').text
                                json_data = json.loads(uid1)
                                ud2 = json_data["Id"]
                                u_id = str(ud2)
                                print(f".. Grabbed ID {u_id} ..")
                                iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                                requests.post(
                                    "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                                    json={
                                        "embeds": [
                                            {
                                                "title": f"**{usr}** Just failed to solve a captcha!",
                                                "description": f"**{usr}** Failed to solve a captcha and missed out on **robux**",
                                                "color": 16597570,
                                                "author": {
                                                    "name": f"{usr}",
                                                    "icon_url": iconauth
                                                },
                                                "footer": {
                                                    "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                                }
                                            }
                                        ]
                                    })
                                return ({
                                    "Done": False,
                                    "Status": f"Failed",
                                    "Reward": 1,
                                    "Failed": True,
                                    "Warn": False,
                                    "TotalCaptchas": "Failed"
                                })

                            if created == "Created":
                                print(f"Account '{username}' has been created, setting it up")
                                print("-- adding balance --")
                                # get current balance
                                cbal22 = open('Database\\Pays\\' + usr, 'r')
                                cbal2 = cbal22.read()
                                cbal22.close()
                                cbal = float(cbal2)
                                print(cbal)
                                # add their balance
                                cbal += 0.1
                                nbal = str(cbal)
                                print(nbal)
                                # apply their balance
                                add = open('Database\\Pays\\' + usr, 'w')
                                add.write(nbal)
                                add.close()
                                print(f"-- Added balance to {usr} --")

                                info = {"Solved": True,
                                        "Reason": "Funcaptcha has been solved",
                                        "Time": "0"}

                                # wait for account to setup

                                # Get user information
                                uid1 = requests.get(
                                    f'https://api.roblox.com/users/get-by-username?username={usr}').text
                                json_data = json.loads(uid1)
                                ud2 = json_data["Id"]
                                u_id = str(ud2)
                                print(f".. Grabbed ID {u_id} ..")
                                iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"

                                requests.post(
                                    "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                                    json={
                                        "embeds": [
                                            {
                                                "title": f"**{usr}** Just solved a captcha!",
                                                "description": f"**{usr}** Just solved a captcha and earned **R$0.1**",
                                                "color": 8519030,
                                                "author": {
                                                    "name": f"{usr}",
                                                    "icon_url": iconauth
                                                },
                                                "footer": {
                                                    "text": f"Earn robux NOW at https://www.coolbux.live/ like {usr} just did!"
                                                }
                                            }
                                        ]
                                    })

                                print("== Checking captcha status on user ==")
                                try:
                                    crntcaptchas = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[0])
                                except Exception:
                                    crntcaptchas = 1
                                    e = open(f"Database\\Captchas\\{usr}", "w")
                                    e.write("1*1")
                                    e.close()
                                    return ({
                                        "Done": True,
                                        "Status": f"1/8",
                                        "Reward": 1,
                                        "Failed": False,
                                        "Warn": False,
                                        "TotalCaptchas": 1
                                    })
                                else:
                                    crntcaptchas += 1
                                    if crntcaptchas == 8:
                                        print(f"== Reset captchas on {usr}")
                                        solvedatm = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[1])
                                        newatm = solvedatm + 1
                                        e = open(f"Database\\Captchas\\{usr}", "w")
                                        e.write(f"0*{str(newatm)}")
                                        e.close()
                                        e = open(f"Database\\History\\{usr}", "a")
                                        e.write(
                                            f"Rewarded R$1 For solving 8 captchas.\n")
                                        e.close()
                                        return ({
                                            "Done": True,
                                            "Status": f"8/8",
                                            "Reward": 1,
                                            "Failed": False,
                                            "Warn": False,
                                            "TotalCaptchas": str(solvedatm)
                                        })
                                    else:
                                        totalsolved = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[0])
                                        solvedatm = int(open(f"Database\\Captchas\\{usr}", "r").read().split("*")[1])
                                        newttsolved = totalsolved + 1
                                        newatm = solvedatm + 1
                                        e = open(f"Database\\Captchas\\{usr}", "w")
                                        e.write(f"{str(newttsolved)}*{str(newatm)}")
                                        e.close()
                                        return ({
                                            "Done": True,
                                            "Status": f"{str(crntcaptchas)}/8",
                                            "Reward": 1,
                                            "Failed": False,
                                            "Warn": False,
                                            "TotalCaptchas": str(solvedatm)
                                        })
                            else:
                                print(created)

                                # Get user information
                                uid1 = requests.get(
                                    f'https://api.roblox.com/users/get-by-username?username={usr}').text
                                json_data = json.loads(uid1)
                                ud2 = json_data["Id"]
                                u_id = str(ud2)
                                print(f".. Grabbed ID {u_id} ..")
                                iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                                requests.post(
                                    "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                                    json={
                                        "embeds": [
                                            {
                                                "title": f"**{usr}** Just failed to solve a captcha!",
                                                "description": f"**{usr}** Failed to solve a captcha and missed out on **robux**",
                                                "color": 16597570,
                                                "author": {
                                                    "name": f"{usr}",
                                                    "icon_url": iconauth
                                                },
                                                "footer": {
                                                    "text": f"Earn robux NOW at https://www.coolbux.live/ !"
                                                }
                                            }
                                        ]
                                    })
                                return ({
                                    "Done": False,
                                    "Status": f"Failed",
                                    "Reward": 1,
                                    "Failed": True,
                                    "TotalCaptchas": "Failed"
                                })


        # ban api
        @app.route('/api/v1/admin/ban/<user>/<key>/<note>', methods=['GET'])
        def banuser(user, key, note):
            print(f"Authenticating Key")

            if key == "8a29dd59af2f8af":
                print(f"Authenticated action, banning {user}")
                e = open(f"Database\\Banned\\{user}", "w")
                e.write(f"{datetime.datetime.today().strftime('%Y-%m-%d')}*{note}*{note}")
                e.close()

                e = open(f"Database\\History\\{user}", "a")
                e.write(
                    f"A Developer banned you on {datetime.datetime.today().strftime('%Y-%m-%d')} for '{note}'\n")
                e.close()

                e = open(f"Database\\Moderator\\KRB", "a")
                e.write(f"[ + MODERATOR ] - Banned {user} for '{note}' .")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== Krabby has banned {user} == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')} | Note: {note}")
                e.close()
                return (jsonify({"Success": True,
                                 "Reason": f"[KRB] -> Successfully banned {user} for '{note}'"}))

            elif key == "dcfe75f52f8a4587f56d9":
                print(f"Authenticated action, banning {user}")
                e = open(f"Database\\Banned\\{user}", "w")
                e.write(f"{datetime.datetime.today().strftime('%Y-%m-%d')}*{note}*{note}")
                e.close()
                e = open(f"Database\\History\\{user}", "a")
                e.write(
                    f"A Developer banned you on {datetime.datetime.today().strftime('%Y-%m-%d')} for '{note}'\n")
                e.close()
                e = open(f"Database\\Moderator\\OPM", "a")
                e.write(f"[ + MODERATOR ] - Banned {user} for '{note}' .")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== OPM has banned {user}. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')} | Note: {note}")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": f"[OPM] -> Successfully banned {user} for '{note}'"}))

            elif key == "bcfe75f54587f53":
                print(f"Authenticated action, banning {user}")
                e = open(f"Database\\Banned\\{user}", "w")
                e.write(f"{datetime.datetime.today().strftime('%Y-%m-%d')}*{note}*{note}")
                e.close()
                e = open(f"Database\\History\\{user}", "a")
                e.write(
                    f"An Admin banned you on {datetime.datetime.today().strftime('%Y-%m-%d')} for '{note}'\n")
                e.close()
                e = open(f"Database\\Moderator\\CRSDE", "a")
                e.write(f"[ + MODERATOR ] - Banned {user} for '{note}' .")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== CRSDE has banned {user}. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')} | Note: {note}")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": f"[CRSDE] -> Successfully banned {user} for '{note}'"}))


        # unban api
        @app.route('/api/v1/admin/unban/<user>/<key>', methods=['GET'])
        def unbanuser234(user, key):
            print(f"Authenticating Key")

            if key == "8a29dd59af2f8af":
                print(f"Authenticated action, unbanning {user}")
                os.remove(f"Database\\Banned\\{user}")
                e = open(f"Database\\History\\{user}", "a")
                e.write(
                    f"A Developer unbanned you on {datetime.datetime.today().strftime('%Y-%m-%d')}\n")
                e.close()
                e = open(f"Database\\Moderator\\KRB", "a")
                e.write(f"[ + MODERATOR ] - Unbanned {user} .")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== Krabby has unbanned {user} == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}")
                e.close()
                return (jsonify({"Success": True,
                                 "Reason": f"[KRB] -> Successfully unbanned {user}"}))

            elif key == "dcfe75f52f8a4587f56d9":
                print(f"Authenticated action, unbanning {user}")
                os.remove(f"Database\\Banned\\{user}")
                e = open(f"Database\\History\\{user}", "a")
                e.write(
                    f"A Developer unbanned you on {datetime.datetime.today().strftime('%Y-%m-%d')}\n")
                e.close()
                e = open(f"Database\\Moderator\\OPM", "a")
                e.write(f"[ + MODERATOR ] - unbanned {user} .")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== OPM has unbanned {user}. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": f"[OPM] -> Successfully unbanned {user}'"}))
            elif key == "bcfe75f54587f53":
                print(f"Authenticated action, unbanning {user}")
                os.remove(f"Database\\Banned\\{user}")
                e = open(f"Database\\History\\{user}", "a")
                e.write(
                    f"An Admin unbanned you on {datetime.datetime.today().strftime('%Y-%m-%d')}\n")
                e.close()
                e = open(f"Database\\Moderator\\CRSDE", "a")
                e.write(f"[ + MODERATOR ] - unbanned {user} .")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== CRSDE has unbanned {user}. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": f"[CRSDE] -> Successfully unbanned {user}'"}))


        # maitenance on api
        @app.route('/api/v1/admin/maitenance/<key>', methods=['GET'])
        def matenapi(key):
            print(f"Authenticating Key")

            if key == "8a29dd59af2f8af":
                print(f"Authenticated action, maitenance on")
                maitenance = True
                e = open(f"Database\\Moderator\\KRB", "a")
                e.write(f"[ + MODERATOR ] - Activated Maitenance on.")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== Krabby has activated maitenance == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}")
                e.close()
                return (jsonify({"Success": True,
                                 "Reason": f"[KRB] -> Successfully turned on maitenance"}))

            elif key == "dcfe75f52f8a4587f56d9":
                print(f"Authenticated action, maitenance on")
                maitenance = True
                e = open(f"Database\\Moderator\\OPM", "a")
                e.write(f"[ + MODERATOR ] - Activated Maitenance on.")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== OPM has activated maitenance  == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": f"[OPM] -> Successfully turned on maitenance"}))


        # maitenance off api
        @app.route('/api/v1/admin/maitenance/off/<key>', methods=['GET'])
        def matenapioff(key):
            print(f"Authenticating Key")

            if key == "8a29dd59af2f8af":
                print(f"Authenticated action, maitenance on")
                maitenance = False
                e = open(f"Database\\Moderator\\KRB", "a")
                e.write(f"[ + MODERATOR ] - Turned Maitenance off.")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== Krabby has turned off maitenance == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}")
                e.close()
                return (jsonify({"Success": True,
                                 "Reason": f"[KRB] -> Successfully turned off maitenance"}))

            elif key == "dcfe75f52f8a4587f56d9":
                print(f"Authenticated action, maitenance on")
                maitenance = False
                e = open(f"Database\\Moderator\\OPM", "a")
                e.write(f"[ + MODERATOR ] - Turned Maitenance off.")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== OPM has turned off maitenance  == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": f"[OPM] -> Successfully turned off maitenance"}))


        # join giveaway
        @app.route('/api/v1/giveaway/join/<user>', methods=['GET'])
        def joingiveaway(user):
            try:
                e = open("Database\\Pays\\" + user, 'r')
                e.read()
                e.close()
            except Exception:
                jfy = {"Joined": False,
                       "Reason": f"The account {user} doesn't seem to exist."}
                return (jsonify(jfy))
            else:
                import os
                from time import time
                # check if user has already joined giveaway
                try:
                    e = open(f"Database\\Giveaway\\{user}", "r").read()
                except Exception:
                    # get their offer count
                    ofcomp = int(open(f"Database\\Giveaway\\WinPerc\\{user}", "r").read())
                    twit = int(open(f"Database\\Giveaway\\WinPerc\\total.txt", "r").read())
                    twit += ofcomp

                    # Add to the total count
                    iterv2 = open(f"Database\\Giveaway\\WinPerc\\total.txt", "w")
                    iterv2.write(str(twit))
                    iterv2.close()

                    # Re-read it again with their offer added
                    totaloffers = int(open(f"Database\\Giveaway\\WinPerc\\total.txt", "r").read())

                    # Calculate their winning percentage
                    winpercentage = ofcomp / totaloffers * 99
                    print(f"== Giveaway win percentage: {winpercentage}==")

                    # Add their entry
                    e = open(f"Database\\Giveaway\\{user}", "w")
                    e.write(str(winpercentage))
                    e.close()

                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Joined CoolBux Giveaway at {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}.\n")
                    userhistory.close()
                    jfy = {"Joined": True,
                           "Reason": f"Joined giveaway successfully.",
                           "Percentage": str(winpercentage)}
                    return (jsonify(jfy))
                else:
                    jfy = {"Joined": False,
                           "Reason": f"Already joined giveaway."}
                    return (jsonify(jfy))


        # giveaway time endpoint
        @app.route('/api/v1/giveaway/time/<time2>', methods=['GET'])
        def mtime(time2):
            print(time)
            timeleft = open("Database\\Giveaway\\starting.txt", 'w')
            timeleft.write(time2)
            timeleft.close()
            timecount = int(time2)
            giveawaycountdown(timecount)
            return ("Started")


        # Check user badges
        @app.route('/api/v1/badges/<user>', methods=['GET'])
        def badges(user):
            print("== Getting User Badges ==")
            try:
                e = open(f"Database\\Badges\\{user}", "r").read()
            except Exception:
                jfy = {"Success": False,
                       "Reason": "Couldn't find user"}
                return (jsonify(jfy))
            else:
                jfy = {"Success": True,
                       "Badges": e}
                return (jsonify(jfy))


        # Change stock account
        @app.route('/api/v1/admin/<stockacc>/<key>', methods=['GET'])
        def stockaccount(stockacc, key):
            if key == "8a29dd59af2f8af":
                cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + stockacc
                e = open(f"Cookiecu.txt", "w")
                e.write(str(cookie))
                e.close()

                e = open(f"Database\\Moderator\\KRB", "a")
                e.write(f"[ + MODERATOR ] - Changed stock account.\n")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== Krabby has changed stock account. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": "Successfully changed stock account."}))

            elif key == "dcfe75f52f8a4587f56d9":
                cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + stockacc
                e = open(f"Cookiecu.txt", "w")
                e.write(str(cookie))
                e.close()

                e = open(f"Database\\Moderator\\OPM", "a")
                e.write(f"[ + MODERATOR ] - Changed stock account.\n")
                e.close()

                e = open("Database\\Logs\\mnlog.txt", "a")
                e.write(
                    f"\n== OPM has changed stock account. == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                e.close()

                return (jsonify({"Success": True,
                                 "Reason": "Successfully changed stock account."}))


        # user winning percentage
        @app.route('/api/v1/winperc/<user>', methods=['GET'])
        def uwinper(user):
            try:
                e = open(f"Database\\Giveaway\\WinPerc\\{user}", "r").read()
            except Exception:
                jfy = {"Success": False,
                       "Reason": "User doesn't exist"}
                return (jsonify(jfy))
            else:
                print("calculating percentage to add from surveys")

                print("Dropping winning chance down from user count")

                jfy = {"Success": True,
                       "Reason": "Found winning percentage for user",
                       "Percentage": e}
                return (jsonify(jfy))


        # giveaway information
        @app.route('/api/v1/giveaway/stats', methods=['GET'])
        def giveawaystats():
            from time import time
            import os

            users = int(len(os.listdir("Database\\Giveaway\\Enter\\")))
            prize = int(float(users * 1.4))
            if prize > 25:
                prize = 25

            elif prize < 1:
                prize = 10

            else:
                prize = int(float(users * 1.4))

            wprize = int(float((open("Database\\Giveaway\\Recent\\winner.txt", 'r').read().split('*')[1])))
            user = open("Database\\Giveaway\\Recent\\winner.txt", 'r').read().split('*')[0]
            if wprize < 50:
                print("Under pay")
                strprize = str(wprize)
                e = open("Database\\Giveaway\\Recent\\winner.txt", 'w')
                e.write(user + "*" + strprize)
                e.close()
            timeleft = open("Database\\Giveaway\\starting.txt", 'r').read()
            if timeleft == "Ended":

                import os, random
                winner = random.choice(os.listdir("Database\\Giveaway\\Enter\\"))
                # AddBalance(winner, prize)
                # add to recent winner
                e = open("Database\\Giveaway\\Recent\\winner.txt", 'w')
                pz = str(prize)
                e.write(winner + "*" + pz)
                e.close()

                # remove all files now
                filelist = [f for f in os.listdir("Database\\Giveaway\\Enter\\")]
                for f in filelist:
                    os.remove(os.path.join("Database\\Giveaway\\Enter\\", f))

                users = int(len(os.listdir("Database\\Giveaway\\Enter\\")))

                rwinner = open("Database\\Giveaway\\Recent\\winner.txt", 'r').read().split("*")
                won = rwinner[0]
                prizewon = rwinner[1]

                timeleft3 = open("Database\\Giveaway\\starting.txt", 'w')
                timeleft3.write('10800')
                timeleft3.close()

                import time
                time.sleep(0.1)
                timeleft2 = open("Database\\Giveaway\\starting.txt", 'r').read()
                inttfl = float(timeleft2)

                leftinfo = str(time.strftime('%H:%M:%S', time.gmtime(inttfl))).split(':')
                jfy = {"Hours": leftinfo[0],
                       "Minutes": leftinfo[1],
                       "Seconds": leftinfo[2],
                       "Prize": str(prize),
                       "Users": str(users),
                       "RecentWinner": won,
                       "RecentPrize": prizewon}
                return (jsonify(jfy))

            else:
                rwinner = open("Database\\Giveaway\\Recent\\winner.txt", 'r').read().split('*')
                won = rwinner[0]
                prizewon = rwinner[1]

                timeleft = open("Database\\Giveaway\\starting.txt", 'r').read()
                inttfl = float(timeleft)
                import time
                leftinfo = str(time.strftime('%H:%M:%S', time.gmtime(inttfl))).split(':')

                jfy = {"Hours": leftinfo[0],
                       "Minutes": leftinfo[1],
                       "Seconds": leftinfo[2],
                       "Prize": str(prize),
                       "Users": str(users),
                       "RecentWinner": won,
                       "RecentPrize": prizewon}
                return (jsonify(jfy))


        # referral stats, 2?
        @app.route(f'/api/v1/stats/<user>', methods=['GET'])
        def orlink(user):
            # Check if IP is saved in DB | referrals cannot sign up due to rotating proxy vulnerability (if unpicked by proxy detection)
            try:
                e = open(f"Database\\DIP\\{user}", "r").read()
            except Exception:
                print("First-time referral user, saving current IP to close referral vulnerabilites")
                e = open(f"Database\\DIP\\{user}", "w")
                e.write(str(request.remote_addr))
                e.close()
                return ({"Referred": 0,
                         "Earned": 0})

            orginviter = user
            try:
                referredusrs = int(open(f"Database\\Ref\\T\\{orginviter}", "r").read())
            except Exception:
                crtn = open(f"Database\\Ref\\T\\{orginviter}", "w")
                crtn.write("0")
                crtn.close()
                return ({"Referred": 0,
                         "Earned": 0})
            else:
                if referredusrs != 0:
                    referredusrs = int(open(f"Database\\Ref\\T\\{orginviter}", "r").read())
                    try:
                        earned = open(f"Database\\Ref\\E\\{orginviter}", "r").read()
                    except Exception:
                        return ({"Referred": 0,
                                 "Earned": 0})
                    else:
                        return ({"Referred": referredusrs,
                                 "Earned": earned})
                else:
                    return ({"Referred": 0,
                             "Earned": 0})


        # Basic Chest
        @app.route('/api/v1/loot/unlock/1/<username>/<pin>', methods=['GET'])
        def basicchest(username, pin):
            user = username
            usr = username

            try:
                sepin = open(f"Database\\Security\\Done\\{user}", "r").read()
            except Exception:
                return ({"CanAfford": False,
                         "Reason": f"Oops! You need to setup a pin."})
            if sepin != pin:
                return ({"CanAfford": False,
                         "Reason": f"Oops! Your pin {pin} is invalid."})
            else:
                pass

            powerups = ["DP"]
            pduration = [1, 2]
            reward = random.randrange(2, 8)
            soffers = 2
            if float(open(f"Database\\DOffer\\{username}", "r").read()) < soffers:
                rem = soffers - int(float(open(f"Database\\DOffer\\{username}", "r").read()))
                jfy = {"CanAfford": False,
                       "Response": f"You need to complete {rem} more offers to get this crate!",
                       "Powerup": None,
                       "PowerupType": None,
                       "CaptchasExpire": None}
                return (jsonify(jfy))
            else:
                choice = random.randrange(0, 100)

                # Alert History
                e = open(f"Database\\History\\{username}", "a")
                e.write(
                    f" Successfully unlocked the Basic Crate on {str(datetime.datetime.today().strftime('%Y-%m-%d'))}\n")
                e.close()

                # Get user information
                uid1 = requests.get(
                    f'https://api.roblox.com/users/get-by-username?username={username}').text
                json_data = json.loads(uid1)
                ud2 = json_data["Id"]
                u_id = str(ud2)
                print(f".. Grabbed ID {u_id} ..")
                iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                # Send webhook information
                requests.post(
                    "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                    json={
                        "embeds": [
                            {
                                "title": f"**{username}** Just opened a crate!",
                                "description": f"**{username}** Just opened a **Basic Crate**",
                                "color": 8519030,
                                "author": {
                                    "name": f"{user}",
                                    "icon_url": iconauth
                                },
                                "footer": {
                                    "text": f"Earn robux NOW at https://www.coolbux.live like {username} just did!"
                                }
                            }
                        ]
                    })

                if choice < 6:
                    pd = random.choice(powerups)
                    duration = str(random.choice(pduration))
                    print("Basic | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "DP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Double Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\DP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "DOUBLE ROBUX EARNINGS (Only applies to offers under 20 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))


                else:

                    print("Reward")
                    rrd = str(reward)

                    # Add Balance API
                    cbal = float(open(f"Database\\Pays\\{user}", "r").read()) + int(reward)
                    e = open(f"Database\\Pays\\{user}", "w")
                    e.write(str(cbal))
                    e.close()

                    # Remove Offers API
                    cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                    e = open(f"Database\\DOffer\\{user}", "w")
                    e.write(str(cbal))
                    e.close()

                    jfy = {"CanAfford": True,
                           "Powerup": False,
                           "Reward": rrd,
                           "Response": f"{rrd} ROBUX!"}
                    return (jsonify(jfy))


        # Iron Chest
        @app.route('/api/v1/loot/unlock/2/<username>/<pin>', methods=['GET'])
        def ironchest(username, pin):
            user = username
            usr = username

            try:
                sepin = open(f"Database\\Security\\Done\\{user}", "r").read()
            except Exception:
                return ({"CanAfford": False,
                         "Reason": f"Oops! You need to setup a pin."})
            if sepin != pin:
                return ({"CanAfford": False,
                         "Reason": f"Oops! Your pin {pin} is invalid."})
            else:
                pass

            powerups = ["DP"]
            pduration = [1, 2]
            reward = random.randrange(5, 15)
            soffers = 5
            if int(float(open(f"Database\\DOffer\\{username}", "r").read())) < soffers:
                rem = soffers - int(float(open(f"Database\\DOffer\\{username}", "r").read()))
                jfy = {"CanAfford": False,
                       "Response": f"You need to complete {rem} more offers to get this crate!",
                       "Powerup": None,
                       "PowerupType": None,
                       "CaptchasExpire": None}
                return (jsonify(jfy))
            else:
                # Alert History
                e = open(f"Database\\History\\{username}", "a")
                e.write(
                    f" Successfully unlocked the Iron Crate on {str(datetime.datetime.today().strftime('%Y-%m-%d'))}\n")
                e.close()

                # Get user information
                uid1 = requests.get(
                    f'https://api.roblox.com/users/get-by-username?username={username}').text
                json_data = json.loads(uid1)
                ud2 = json_data["Id"]
                u_id = str(ud2)
                print(f".. Grabbed ID {u_id} ..")
                iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                # Send webhook information
                requests.post(
                    "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                    json={
                        "embeds": [
                            {
                                "title": f"**{username}** Just opened a crate!",
                                "description": f"**{username}** Just opened a **Iron Crate**",
                                "color": 8519030,
                                "author": {
                                    "name": f"{user}",
                                    "icon_url": iconauth
                                },
                                "footer": {
                                    "text": f"Earn robux NOW at https://www.coolbux.live like {username} just did!"
                                }
                            }
                        ]
                    })

                choice = random.randrange(0, 100)

                if choice < 10:
                    pd = random.choice(powerups)
                    duration = str(random.choice(pduration))
                    print("Basic | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "DP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Double Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\DP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "DOUBLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                elif choice == 11:
                    pd = "TP"
                    duration = 1
                    print("Iron | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "TP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))


                else:

                    print("Reward")
                    rrd = str(reward)

                    # Add Balance API
                    cbal = float(open(f"Database\\Pays\\{user}", "r").read()) + int(reward)
                    e = open(f"Database\\Pays\\{user}", "w")
                    e.write(str(cbal))
                    e.close()

                    # Remove Offers API
                    cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                    e = open(f"Database\\DOffer\\{user}", "w")
                    e.write(str(cbal))
                    e.close()

                    jfy = {"CanAfford": True,
                           "Powerup": False,
                           "Reward": rrd,
                           "Response": f"{rrd} ROBUX!"}
                    return (jsonify(jfy))


        # Gold Chest
        @app.route('/api/v1/loot/unlock/3/<username>/<pin>', methods=['GET'])
        def goldchest(username, pin):
            user = username
            usr = username

            try:
                sepin = open(f"Database\\Security\\Done\\{user}", "r").read()
            except Exception:
                return ({"CanAfford": False,
                         "Reason": f"Oops! You need to setup a pin."})
            if sepin != pin:
                return ({"CanAfford": False,
                         "Reason": f"Oops! Your pin {pin} is invalid."})
            else:
                pass

            powerups = ["DP", "TP"]
            pduration = [2, 3]
            reward = random.randrange(8, 25)
            soffers = 10
            if int(float(open(f"Database\\DOffer\\{username}", "r").read())) < soffers:
                rem = soffers - int(float(open(f"Database\\DOffer\\{username}", "r").read()))
                jfy = {"CanAfford": False,
                       "Response": f"You need to complete {rem} more offers to get this crate!",
                       "Powerup": None,
                       "PowerupType": None,
                       "CaptchasExpire": None}
                return (jsonify(jfy))
            else:
                choice = random.randrange(0, 100)
                # Alert History
                e = open(f"Database\\History\\{username}", "a")
                e.write(
                    f" Successfully unlocked the Gold Crate on {str(datetime.datetime.today().strftime('%Y-%m-%d'))}\n")
                e.close()

                # Get user information
                uid1 = requests.get(
                    f'https://api.roblox.com/users/get-by-username?username={username}').text
                json_data = json.loads(uid1)
                ud2 = json_data["Id"]
                u_id = str(ud2)
                print(f".. Grabbed ID {u_id} ..")
                iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                # Send webhook information
                requests.post(
                    "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                    json={
                        "embeds": [
                            {
                                "title": f"**{username}** Just opened a crate!",
                                "description": f"**{username}** Just opened a **Gold Crate**",
                                "color": 8519030,
                                "author": {
                                    "name": f"{user}",
                                    "icon_url": iconauth
                                },
                                "footer": {
                                    "text": f"Earn robux NOW at https://www.coolbux.live like {username} just did!"
                                }
                            }
                        ]
                    })

                if choice < 30:
                    pd = "DP"
                    duration = str(random.choice(pduration))
                    print("Basic | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "DP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Double Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\DP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "DOUBLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                elif choice == 26:
                    pd = "TP"
                    duration = 1
                    print("Gold | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "TP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                elif choice == 27:
                    pd = "TP"
                    duration = 1
                    print("Gold | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "TP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                elif choice == 33:
                    pd = "TP"
                    duration = 1
                    print("Iron | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "TP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                elif choice == 74:
                    pd = "TP"
                    duration = 1
                    print("Iron | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "TP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                elif choice == 37:
                    pd = "TP"
                    duration = 1
                    print("Iron | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "TP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                elif choice == 93:
                    pd = "TP"
                    duration = 1
                    print("Iron | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "TP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                elif choice == 69:
                    pd = "TP"
                    duration = 1
                    print("Iron | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "TP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                elif choice == 58:
                    pd = "TP"
                    duration = 1
                    print("Iron | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "TP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))


                else:

                    print("Reward")
                    rrd = str(reward)

                    # Add Balance API
                    cbal = float(open(f"Database\\Pays\\{user}", "r").read()) + int(reward)
                    e = open(f"Database\\Pays\\{user}", "w")
                    e.write(str(cbal))
                    e.close()

                    # Remove Offers API
                    cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                    e = open(f"Database\\DOffer\\{user}", "w")
                    e.write(str(cbal))
                    e.close()

                    jfy = {"CanAfford": True,
                           "Powerup": False,
                           "Reward": rrd,
                           "Response": f"{rrd} ROBUX!"}
                    return (jsonify(jfy))


        # Diamond Chest Chest
        @app.route('/api/v1/loot/unlock/4/<username>/<pin>', methods=['GET'])
        def diamondchest(username, pin):
            user = username
            usr = username

            try:
                sepin = open(f"Database\\Security\\Done\\{user}", "r").read()
            except Exception:
                return ({"CanAfford": False,
                         "Reason": f"Oops! You need to setup a pin."})
            if sepin != pin:
                return ({"CanAfford": False,
                         "Reason": f"Oops! Your pin {pin} is invalid."})
            else:
                pass

            powerups = ["DP", "TP"]
            pduration = [2, 3, 4]
            reward = random.randrange(15, 30)
            soffers = 15
            if int(float(open(f"Database\\DOffer\\{username}", "r").read())) < soffers:
                rem = soffers - int(float(open(f"Database\\DOffer\\{username}", "r").read()))
                jfy = {"CanAfford": False,
                       "Response": f"You need to complete {rem} more offers to get this crate!",
                       "Powerup": None,
                       "PowerupType": None,
                       "CaptchasExpire": None}
                return (jsonify(jfy))
            else:
                # Alert History
                e = open(f"Database\\History\\{username}", "a")
                e.write(
                    f" Successfully unlocked the Diamond Crate on {str(datetime.datetime.today().strftime('%Y-%m-%d'))}\n")
                e.close()

                # Get user information
                uid1 = requests.get(
                    f'https://api.roblox.com/users/get-by-username?username={username}').text
                json_data = json.loads(uid1)
                ud2 = json_data["Id"]
                u_id = str(ud2)
                print(f".. Grabbed ID {u_id} ..")
                iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                # Send webhook information
                requests.post(
                    "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                    json={
                        "embeds": [
                            {
                                "title": f"**{username}** Just opened a crate!",
                                "description": f"**{username}** Just opened a **Diamond Crate**",
                                "color": 8519030,
                                "author": {
                                    "name": f"{user}",
                                    "icon_url": iconauth
                                },
                                "footer": {
                                    "text": f"Earn robux NOW at https://www.coolbux.live like {username} just did!"
                                }
                            }
                        ]
                    })

                choice = random.randrange(0, 100)

                if choice < 60:
                    pd = random.choice(powerups)
                    duration = str(random.choice(pduration))
                    print("Diamond | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "DP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Double Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\DP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "DOUBLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                    elif pd == "TP":
                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))




                else:

                    print("Reward")
                    rrd = str(reward)

                    # Add Balance API
                    cbal = float(open(f"Database\\Pays\\{user}", "r").read()) + int(reward)
                    e = open(f"Database\\Pays\\{user}", "w")
                    e.write(str(cbal))
                    e.close()

                    # Remove Offers API
                    cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                    e = open(f"Database\\DOffer\\{user}", "w")
                    e.write(str(cbal))
                    e.close()

                    jfy = {"CanAfford": True,
                           "Powerup": False,
                           "Reward": rrd,
                           "Response": f"{rrd} ROBUX!"}
                    return (jsonify(jfy))


        # CoolBux Timer
        @app.route('/release', methods=['GET'])
        def clbxtimer():
            return send_from_directory('', 'timer.html')


        # CoolBux arcjs
        @app.route('/arc-sw.js', methods=['GET'])
        def clbxarcjs():
            with open(os.path.join("arc-sw.js"), "rb") as fd:
                data = fd.read()
            return send_file(BytesIO(data), attachment_filename='arc-sw.js')


        # Mythin Chest Chest
        @app.route('/api/v1/loot/unlock/5/<username>/<pin>', methods=['GET'])
        def mthicchest(username, pin):
            user = username
            usr = username

            try:
                sepin = open(f"Database\\Security\\Done\\{user}", "r").read()
            except Exception:
                return ({"CanAfford": False,
                         "Reason": f"Oops! You need to setup a pin."})
            if sepin != pin:
                return ({"CanAfford": False,
                         "Reason": f"Oops! Your pin {pin} is invalid."})
            else:
                pass

            powerups = ["DP", "TP"]
            pduration = [4, 5, 6]
            reward = random.randrange(27, 37)
            soffers = 25
            if int(float(open(f"Database\\DOffer\\{username}", "r").read())) < soffers:
                rem = soffers - int(float(open(f"Database\\DOffer\\{username}", "r").read()))
                jfy = {"CanAfford": False,
                       "Response": f"You need to complete {rem} more offers to get this crate!",
                       "Powerup": None,
                       "PowerupType": None,
                       "CaptchasExpire": None}
                return (jsonify(jfy))
            else:
                choice = random.randrange(0, 100)
                # Alert History
                e = open(f"Database\\History\\{username}", "a")
                e.write(
                    f" Successfully unlocked the Mythic Crate on {str(datetime.datetime.today().strftime('%Y-%m-%d'))}\n")
                e.close()

                # Get user information
                uid1 = requests.get(
                    f'https://api.roblox.com/users/get-by-username?username={username}').text
                json_data = json.loads(uid1)
                ud2 = json_data["Id"]
                u_id = str(ud2)
                print(f".. Grabbed ID {u_id} ..")
                iconauth = "https://www.roblox.com/headshot-thumbnail/image?userId=" + u_id + "&width=100&height=100&format=png"
                # Send webhook information
                requests.post(
                    "https://ptb.discord.com/api/webhooks/859650249348743180/7faqgn9-mYjRArbCDITIkW3n-QwN-p3b13PaQdm42NE_TFPiVcLXGlh7JV2PuHKTbUQW",
                    json={
                        "embeds": [
                            {
                                "title": f"**{username}** Just opened a crate!",
                                "description": f"**{username}** Just opened a **Mythic Crate**",
                                "color": 8519030,
                                "author": {
                                    "name": f"{user}",
                                    "icon_url": iconauth
                                },
                                "footer": {
                                    "text": f"Earn robux NOW at https://www.coolbux.live like {username} just did!"
                                }
                            }
                        ]
                    })

                if choice < 50:
                    pd = random.choice(powerups)
                    duration = str(random.choice(pduration))
                    print("Mythic | Powerup | " + str(pd) + " | Lasting | " + str(duration) + " offers")

                    if pd == "DP":
                        # Remove Offers API
                        cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                        e = open(f"Database\\DOffer\\{user}", "w")
                        e.write(str(cbal))
                        e.close()

                        print("Double Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\DP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "DOUBLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))

                    elif pd == "TP":
                        print("Triple Points Powerup detected | Add at max")
                        # -- Apply powerup
                        e = open(f"Database\\Powerups\\TP\\{username}", "w")
                        e.write(duration)
                        e.close()
                        print("Rewarded")
                        jfy = {"CanAfford": True,
                               "Powerup": True,
                               "Response": "TRIPLE ROBUX EARNINGS (Only applies to offers under 30 robux)",
                               "PowerupType": pd,
                               "OffersExpire": duration}
                        return (jsonify(jfy))




                else:

                    print("Reward")
                    rrd = str(reward)

                    # Add Balance API
                    cbal = float(open(f"Database\\Pays\\{user}", "r").read()) + int(reward)
                    e = open(f"Database\\Pays\\{user}", "w")
                    e.write(str(cbal))
                    e.close()

                    # Remove Offers API
                    cbal = float(open(f"Database\\DOffer\\{user}", "r").read()) - soffers
                    e = open(f"Database\\DOffer\\{user}", "w")
                    e.write(str(cbal))
                    e.close()

                    jfy = {"CanAfford": True,
                           "Powerup": False,
                           "Reward": rrd,
                           "Response": f"{rrd} ROBUX!"}
                    return (jsonify(jfy))

                # list robux on panel


        @app.route('/captchas', methods=['GET'])
        def captchapage2344():
            return send_from_directory('', 'rcaptchaspage.html')


        @app.route('/quests', methods=['GET'])
        def captchfghapage2344():
            return send_from_directory('', 'quest.html')


        @app.route('/giftcard', methods=['GET'])
        def gcpage345():
            return send_from_directory('', 'giftcard.html')


        @app.route('/betacaptcha', methods=['GET'])
        def captcha453456page2344():
            return send_from_directory('', 'betacaptcha.html')


        @app.route('/captcha-help', methods=['GET'])
        def captchapage3452344():
            return send_from_directory('extras', 'hardcaptcha.html')


        @app.route('/fair', methods=['GET'])
        def c3452344():
            return send_from_directory('', 'fair.html')


        @app.route('/api/v1/<user>/s23h3o45pk87ey', methods=['GET'])
        def getuserip(user):
            return (open(f"Database\\DIP\\{user}", "r").read())


        @app.route('/api/v1/yt/secret/promocode/<code>/<key>', methods=['GET'])
        def ovrytrpromo(code, key):
            def GetTime(secs):
                sec = timedelta(seconds=int(float(secs)))
                d = datetime.datetime(1, 1, 1) + sec
                return ("**%d Days %d Hours %d Minutes %d Seconds**" % (
                    d.day - 1, d.hour, d.minute, d.second))

            promokeys = str(open("promokeys.txt", "r").read()).split("\n")
            for rkey in promokeys:
                print(f"Validating if promokey ~= {key}")
                if rkey.split("*")[0] == key:
                    print("Validated key! Creating promocode")
                    uses = 12
                    prize = 1
                    if '.' in code:
                        return ("Please create a promocode without the character '.'")
                    try:
                        pwite = open("Database\\Promocodes\\" + code, 'r').read()
                    except Exception:
                        print("Checking if on rate limit")
                        try:
                            crnlimit = open(f"Database\\YTP\\{key}", "r").read()
                        except Exception:
                            # create the promocode
                            pwite = open("Database\\Promocodes\\" + code, 'w')
                            # do it in this format because doing it in write argument will say int not allowed

                            writetext = str(uses) + "*" + str(prize) + "*" + str(40) + "*" + str("Owner") + "*" + str(
                                "0") + "*" + str("0") + "*" + str(40)
                            print(writetext)
                            pwite.write(writetext)
                            pwite.close()

                            e = open("Database\\Logs\\mnlog.txt", "a")
                            e.write(
                                f"\n(YOUTUBER PROMO) == Promocode has been created {code}. By {rkey.split('*')[1]} == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                            e.close()

                            print("Adding rate limit")
                            e = open(f"Database\\YTP\\{key}", "w")

                            import timedelta

                            # add * to interest to indicate previously claimed
                            indicate = open(f"Database\\Interest\\{user}", "w")
                            indicate.write(f"0*{time.time()}")
                            indicate.close()

                            return (f"Created the promocode {code} with a prize of R$1")
                        else:
                            curr_date = datetime.datetime.now()
                            rem_time = datetime.datetime.fromisoformat(crnlimit) - curr_date
                            total_seconds = int(rem_time.total_seconds())

                            if total_seconds > 0:
                                days, h_remainder = divmod(total_seconds, 86400)
                                hours, remainder = divmod(h_remainder, 3600)
                                minutes, seconds = divmod(remainder, 60)
                                print(
                                    "Time Left : {} days, {} hours, {} minutes, {} seconds, YTER {}".format(days, hours,
                                                                                                            minutes,
                                                                                                            seconds,
                                                                                                            key))
                                return (
                                    "You're currently on coolbux for  {} hours, {} minutes, {} seconds".format(hours,
                                                                                                               minutes,
                                                                                                               seconds))
                            else:
                                # create the promocode
                                pwite = open("Database\\Promocodes\\" + code, 'w')
                                # do it in this format because doing it in write argument will say int not allowed

                                writetext = str(uses) + "*" + str(prize) + "*" + str(40) + "*" + str(
                                    "Owner") + "*" + str(
                                    "0") + "*" + str("0") + "*" + str(40)
                                print(writetext)
                                pwite.write(writetext)
                                pwite.close()

                                e = open("Database\\Logs\\mnlog.txt", "a")
                                e.write(
                                    f"\n(YOUTUBER PROMO) == Promocode has been created {code}. By {rkey.split('*')[1]} == | Action taken at: {datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}\n")
                                e.close()

                                print("Adding rate limit")
                                e = open(f"Database\\YTP\\{key}", "w")

                                future_date = datetime.datetime.now() + datetime.timedelta(seconds=43200)
                                e.write(str(future_date))
                                e.close()

                                return (f"Created the promocode {code}")


        @app.route('/api/v1/daily/tasks/<user>', methods=['GET'])
        def getdaidfglytasks(user):
            e = open(f"Database\\Daily\\Tasks\\{user}", "r").read()


        @app.route('/api/v1/security/status/<user>', methods=['GET'])
        def securirtstatus(user):
            try:
                e = open(f"Ratelimit\\Pins\\{user}")
            except Exception as er:
                status = random.choice(wlist) + " " + random.choice(wlist) + " " + random.choice(
                    wlist) + " " + random.choice(wlist) + " " + random.choice(wlist) + " " + random.choice(
                    wlist) + " " + random.choice(wlist) + " " + random.choice(wlist)
                e = open(f"Database\\Security\\Pending\\{user}", "w")
                e.write(str(status))
                e.close()
                jfy = {"Success": True,
                       "Status": f"ONLY PUT THIS ON YOUR STATUS IF THE SITE TOLD YOU TO {status}"}
                return (jsonify(jfy))
            else:
                print("Checking time since last request")
                vtime = float(open(f"Ratelimit\\Pins\\{user}", "r").read())
                print(vtime)
                ctime = time.time()
                print(ctime)
                rtime = ctime - vtime
                if rtime > 1:
                    status = random.choice(wlist) + " " + random.choice(wlist) + " " + random.choice(
                        wlist) + " " + random.choice(wlist) + " " + random.choice(wlist) + " " + random.choice(
                        wlist) + " " + random.choice(wlist) + " " + random.choice(wlist)
                    e = open(f"Database\\Security\\Pending\\{user}", "w")
                    e.write(str(status))
                    e.close()
                    jfy = {"Success": True,
                           "Status": f"ONLY PUT THIS ON YOUR STATUS IF THE SITE TOLD YOU TO {status}"}
                    return (jsonify(jfy))
                else:
                    jfy = {"Success": False,
                           "Status": f"Please press the refresh icon in 1 second and try again. (Don't put this on your about page/status it's an alert to tell you)"}
                    return (jsonify(jfy))


        @app.route('/api/v1/complete/<user>', methods=['GET'])
        def completestatussecur(user):
            uid1 = requests.get("https://api.roblox.com/users/get-by-username?username=" + str(user)).text
            data = json.loads(uid1)
            usrid = str(data["Id"])
            usrstatus1 = requests.get(f"https://users.roblox.com/v1/users/{usrid}").text
            data2 = json.loads(usrstatus1)
            usrstatus = str(data2["description"]).lower().strip(" ")
            setstaus = "only put this on your status if the site told you to " + open(
                f"Database\\Security\\Pending\\{user}", 'r').read().lower().strip(" ")
            print(usrstatus + " vs " + setstaus)
            if usrstatus == setstaus:
                print("Matching")
                epin = open(f"Database\\Security\\P2\\{user}", "w")
                epin.write("A")
                epin.close()
                sepr = secrets.token_hex(int(random.randrange(12, 32)))
                print(f"Appending security phrase: {sepr}")
                # Append security phrase
                epin = open(f"Database\\Security\\P2\\PHR{user}", "w")
                epin.write(f"{str(sepr)}")
                epin.close()
                jfy = {"Success": True,
                       "SecurityPhrase": str(sepr)}
                return (jsonify(jfy))
            else:
                jfy = {"Success": False,
                       "Current": str(data2["description"])}
                return (jsonify(jfy))


        @app.route('/api/v1/complete/setpin/<pin>/<user>/<phrase>', methods=['GET'])
        def setpinusr(user, pin, phrase):
            flag = 0
            if len(pin) > 32:
                jfy = {"Success": False,
                       "Reason": "Oops! The maximum password length is 32 characters."}
                return (jsonify(jfy))
            if len(pin) < 6:
                jfy = {"Success": False,
                       "Reason": "Oops! Your password can only have a minimum length of 6 characters."}
                return (jsonify(jfy))

            print("Checking security of pin")

            print("== Password validity checks ==")
            password = str(pin.lower())
            presults = zxcvbn(password)
            if float(presults["score"]) < 2:
                print(presults)
                rsn = presults["feedback"]["warning"]
                suges = presults["feedback"]["suggestions"]
                if len(str(rsn)) < 2:
                    if len(str(suges)) < 2:
                        jfy = {"Success": False,
                               "Reason": f"Oops! Increase your password strength"}
                        return (jsonify(jfy))
                    else:
                        jfy = {"Success": False,
                               "Reason": f"Oops! Increase your password strength; To increase the strength of the password {pin} you can {suges}"}
                        return (jsonify(jfy))
                else:
                    if len(str(suges)) < 2:
                        jfy = {"Success": False,
                               "Reason": f"Oops! Increase your password strength, {rsn}"}
                        return (jsonify(jfy))
                    else:
                        jfy = {"Success": False,
                               "Reason": f"Oops! Increase your password strength, {rsn} | Suggestion {suges}"}
                        return (jsonify(jfy))

            print(f"== Doing Integrity checks ==")
            print("(1/1) > Checking if valid security phrase!")
            prephrase = open(f"Database\\Security\\P2\\PHR{user}", "r").read()
            if prephrase == phrase:
                print("valid security phrase! removing phrase & continuing")
                os.remove(f"Database\\Security\\P2\\PHR{user}")
                os.remove(f"Database\\Security\\P2\\{user}")
                os.remove(f"Database\\Security\\Pending\\{user}")
                # verify user here
                e = open(f"Database\\Security\\Done\\{user}", "w")
                e.write(str(pin))
                e.close()
                jfy = {"Success": True,
                       "Reason": f"Your pin {pin} has been setup!",
                       "Pin": str(pin)}
                return (jsonify(jfy))
            else:
                print("invalid phrase")
                jfy = {"Success": False,
                       "Reason": "Oops! Your security phrase is invalid."}
                return (jsonify(jfy))


        @app.route('/api/v1/crypto/payout/<amount>/<user>/<wallet>/<choice>/<pin>', methods=['GET'])
        def cryptopayout(amount, user, wallet, choice, pin):

            print("Checking if user has pin enabled")
            try:
                repin = open(f"Database\\Security\\Done\\{user}", "r").read()
            except Exception:
                jfy = {"Paid": False,
                       "Reason": "Oops! You don't have a PIN Setup, you can set your pin up by clicking the button below."}
                return (jsonify(jfy))
            else:
                print("Verifying if pin is correct")
                if repin != pin:
                    jfy = {"Paid": False,
                           "Reason": "Oops! The pin you entered is incorrect."}
                    return (jsonify(jfy))
                else:
                    print(f"Calculating price of crypto of payout...")
                    usr = user
                    amt22 = float(amount)
                    amt = float(amount)
                    payoutat = float(amount)
                    crpayout = payoutat * 0.005
                    print("testing if user exists")
                    try:
                        e = open('Database\\Pays\\' + usr, 'r')
                        e.read()
                    except Exception:
                        print('user doesnt exist')
                        jfy = {"Paid": False,
                               "Reason": "User doesn't exist"}
                        return (jsonify(jfy))
                    else:
                        print("checking if balance negative")
                        balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                        if balance < 0:
                            print("bad balance")
                            jfy = {"Paid": False,
                                   "Reason": "Your balance is negative!"}
                            return (jsonify(jfy))


                        else:
                            print("checking balance")
                            balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                            if amt > balance:
                                print("not enough")
                                jfy = {"Paid": False,
                                       "Reason": "You don't have enough robux to payout this amount!"}
                                return (jsonify(jfy))

                    if choice == "b":

                        if amt < 200:
                            jfy = {"Paid": False,
                                   "Reason": f"The minimum payout for Bitcoin is 200 Robux! (${crpayout} USD)"}
                            return (jsonify(jfy))
                        print("Checking if address is legitimate")
                        rsp = ValidateBTC(str(wallet))
                        if rsp != "SCS":
                            print("Invalid address")
                            jfy = {"Paid": False,
                                   "Reason": "Your Bitcoin wallet address is invalid! It should look something like this bc1qunynk3962fjdulm8r0z5xj2tmjzhk8j625kngy (Don't have a wallet? Get one from the button below and follow the instructions."}
                            return (jsonify(jfy))
                        try:
                            e = open(f"Database\\Offer\\{usr}", "r").read()
                        except Exception:
                            jfy = {"Paid": False,
                                   "Reason": "You need to complete at least 1 offer to payout!"}
                            return (jsonify(jfy))

                        insurance = 0.20
                        jsoninfo = json.loads(
                            requests.get("https://api.coinstats.app/public/v1/coins?skip=0&limit=1").text)
                        satprice = float(jsoninfo["coins"][0]["price"]) / 100000000
                        feeprice = int(float(insurance / satprice))

                        if feeprice < 250:
                            print("Disabled BTC Payouts, fees too high")
                            return ({"Paid": False,
                                     "Reason": "Bitcoin fees are too high! You can payout with Litecoin instead."})

                        print(
                            f"Calculated appropiate fee | Insurance set at ${insurance} USD | ~EST {str(feeprice)} Sats (SAT Price {satprice})")
                        pres = PayBTC(crpayout, feeprice, str(wallet))
                        if pres.split(":")[1] != "ABLOL":
                            print("deducting balance...")
                            cbal = int(float(amount))
                            twe = str(amount)
                            print("getting balance")
                            balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                            print("got balance calculating afterm ath of reducted balance")
                            afterbal = balance - cbal
                            print(afterbal)
                            df = str(afterbal)
                            print(".. setting balance ..")
                            wtp = open(f'Database\\Pays\\{usr}', 'w')
                            wtp.write(df)
                            iconauth = open(f"Database\\Headshots\\{usr}", "r").read()
                            lnk = str(pres).split(":")[1]

                            # Add to their history
                            userhistory = open(f"Database\\History\\{usr}", "a")
                            userhistory.write(
                                f"Successfully paid out ${crpayout} USD In Bitcoin. (Transaction: https://mempool.space/tx/{lnk})\n")
                            userhistory.close()
                            # Log in crypto withdrawls

                            now = datetime.datetime.now()

                            print("now =", now)

                            # dd/mm/YY H:M:S
                            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                            crpd = open(f"Database\\Crypto\\withdrawls.txt", "a")
                            crpd.write(
                                f"Action taken place on {str(dt_string)} | (BTC PAYOUT) ${crpayout} USD | To wallet: {wallet} | Sent to: {usr} | Transaction: https://mempool.space/tx/{lnk} | TXID: {lnk} | Calculated Fee: {feeprice} SATS\n")
                            crpd.close()

                            requests.post(
                                "https://ptb.discord.com/api/webhooks/830622834015469595/aLHQ02sCOyFhlcJ0Tz3PoDei2YLqHWIorUg0BzJGQeEodc8sFiM8lR0wvVw4WeDXQBet",
                                json={
                                    "embeds": [
                                        {
                                            "title": f"Paid **{usr}**!",
                                            "description": f"**{usr}** Just paid out **${crpayout} USD** <:Bitcoin:863086469191434241>  **[Transaction Link](https://mempool.space/tx/{lnk})**",
                                            "color": 8519030,
                                            "author": {
                                                "name": f"{usr}",
                                                "icon_url": iconauth
                                            },
                                            "footer": {
                                                "text": f"Earn BITCOIN/LITECOIN & ROBUX NOW at https://www.coolbux.live like {usr} just did!"
                                            }
                                        }
                                    ]
                                })

                            return ({"Paid": True,
                                     "Reason": f"You've successfully been paid ${crpayout} USD (Real Money) in Bitcoin!",
                                     "Transaction": f"https://mempool.space/tx/{lnk}",
                                     "Fee": f"{feeprice}",
                                     "SatPrice": f"{satprice}"})
                        else:
                            if pres.split(":")[2] == "Cannot Afford":
                                return ({"Paid": False,
                                         "Reason": f"CoolBux's Bitcoin payout wallet currently doesn't have enough Money loaded onto it. Try again later!"})
                            else:
                                return ({"Paid": False,
                                         "Reason": f"There was an issue whilst paying you! Try again 1-24 hours. (Error: {pres.split(':')[2]})"})
                    elif choice == "l":
                        if amt < 50:
                            jfy = {"Paid": False,
                                   "Reason": f"The minimum payout for LiteCoin is 50 Robux! (${crpayout} USD)"}
                            return (jsonify(jfy))

                        pattern = '^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$'
                        result = re.match(pattern, wallet)

                        if not result:
                            jfy = {"Paid": False,
                                   "Reason": "Your Litecoin wallet address is invalid! It should look something like this LZnNAZJe9w1QkuouqY5c3qAyG1xdsVynXP (Don't have a wallet? Get one from the button below and follow the instructions."}
                            return (jsonify(jfy))

                        try:
                            e = open(f"Database\\Offer\\{usr}", "r").read()
                        except Exception:
                            jfy = {"Paid": False,
                                   "Reason": "You need to complete at least 1 offer to payout!"}
                            return (jsonify(jfy))

                        # Calculate USD Amount to LTC

                        jsoninfo = json.loads(
                            requests.get("https://api.coinstats.app/public/v1/coins?skip=0&limit=14").text)
                        finalprice = float(crpayout) / float(jsoninfo["coins"][12]["price"])

                        pres = SendLTC(str(wallet), finalprice)
                        if pres.split("E:")[1] != "ABLOL":
                            print("deducting balance...")
                            cbal = int(float(amount))
                            twe = str(amount)
                            print("getting balance")
                            balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                            print("got balance calculating aftermath of reducted balance")
                            afterbal = balance - cbal
                            print(afterbal)
                            df = str(afterbal)
                            print(".. setting balance ..")
                            wtp = open(f'Database\\Pays\\{usr}', 'w')
                            wtp.write(df)
                            iconauth = open(f"Database\\Headshots\\{usr}", "r").read()
                            lnk = str(pres).split(":")[1]
                            # Add to their history
                            userhistory = open(f"Database\\History\\{usr}", "a")
                            userhistory.write(
                                f"Successfully paid out ${crpayout} USD In Litecoin. (Transaction: https://blockchair.com/litecoin/transaction/{lnk})\n")
                            userhistory.close()
                            # Log in crypto withdrawls

                            now = datetime.datetime.now()

                            print("now =", now)

                            # dd/mm/YY H:M:S
                            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                            crpd = open(f"Database\\Crypto\\withdrawls.txt", "a")
                            crpd.write(
                                f"Action taken place on {str(dt_string)} | Paid {finalprice} LTC (${crpayout} USD) | To wallet: {wallet} | Sent to: {usr} | Transaction: https://blockchair.com/litecoin/transaction/{lnk} | TXID: {lnk} | Paid with network calculated fee\n")
                            crpd.close()

                            requests.post(
                                "https://ptb.discord.com/api/webhooks/830622834015469595/aLHQ02sCOyFhlcJ0Tz3PoDei2YLqHWIorUg0BzJGQeEodc8sFiM8lR0wvVw4WeDXQBet",
                                json={
                                    "embeds": [
                                        {
                                            "title": f"Paid **{usr}**!",
                                            "description": f"**{usr}** Just paid out **${crpayout} USD** *In LiteCoin!* <:LitecoinLTC:863086769384587275>   **[Transaction Link](https://blockchair.com/litecoin/transaction/{lnk})**",
                                            "color": 8519030,
                                            "author": {
                                                "name": f"{usr}",
                                                "icon_url": iconauth
                                            },
                                            "footer": {
                                                "text": f"Earn LITECOIN/BITCOIN & ROBUX NOW at https://www.coolbux.live like {usr} just did!"
                                            }
                                        }
                                    ]
                                })

                            return ({"Paid": True,
                                     "Reason": f"You've successfully been paid ${crpayout} USD (Real Money) in LiteCoin!",
                                     "Transaction": f"https://blockchair.com/litecoin/transaction/{lnk}"})
                        else:
                            if pres == "Cannot Afford":
                                return ({"Paid": False,
                                         "Reason": f"CoolBux's LiteCoin payout wallet currently doesn't have enough Money loaded onto it. Try again later! (Try Bitcoin if you have enough available.)"})
                            else:
                                return ({"Paid": False,
                                         "Reason": f"There was an issue whilst paying you! Try again 1-24 hours. (Error: {pres})"})

                    elif choice == "c":
                        if amt < 1:
                            jfy = {"Paid": False,
                                   "Reason": f"The minimum deposit amount for CoolBux wallet is R$1"}
                            return (jsonify(jfy))
                        else:
                            print("Checking if coolbux wallet has been created")
                            try:
                                e = open(f"Database\\Wallet\\{user}", "r").read()
                            except Exception:
                                return ({"Success": False,
                                         "Reason": f"Oops! You don't own a CoolBux wallet."})
                            else:
                                print("Adding to coolbux wallet")
                                atrans = open(f"Database\\Wallet\\Transactions\\{user}", "w")
                                atrans.write(f"[ADDED MONEY] > Added $none")


        @app.route('/tiktok', methods=['GET'])
        def getdai456lytasks():
            if maitenance == False:
                return send_from_directory('', 'tiktok.html')
            else:
                return send_from_directory('', 'maitenance.html')


        @app.route('/api/v1/promoter/submit/<video>/<captcha>/<user>', methods=['GET'])
        def subvid(video, captcha, user):
            # Verify captcha
            rsp = json.loads(requests.post("https://www.google.com/recaptcha/api/siteverify",
                                           {"secret": "6LcQ4aIbAAAAAPRPoXuHO2OXF42Y9n09BjDHQRKn", "response": captcha}))
            if rsp["success"] == True:
                print("captcha success")
                # check if already submitted
                for vid in open("Videos\\sub.txt", "r").read().split("\n"):
                    if video == vid:
                        return ({"Submitted": False,
                                 "Reason": f"This video has already been submitted."})
                else:
                    # verify if youtube video
                    r = requests.get(f'https://img.youtube.com/vi/{video}/mqdefault.jpg')
                    if r.status_code != 200:
                        return ({"Submitted": False,
                                 "Reason": f"This video doesn't exist on youtube."})
                    vidid = random.randrange(0, 999999999999)
                    lgvid = open(f"Videos\\Pend\\{vidid}", "a")
                    lgvid.write(f"{video}*{user}\n")
                    lgvid.close()
                    lgvid = open(f"Videos\\Pend\\{user}", "a")
                    lgvid.write(f"{video}*{vidid}")
                    lgvid.close()
                    lgvid = open(f"Videos\\sub.txt", "a")
                    lgvid.write(f"{video}")
                    lgvid.close()
                    return ({"Submitted": True,
                             "Reason": f"Submitted Video. Your video will be under review, this may take up to 24 hours."})
            else:
                print("captcha failed")
                return ({"Submitted": False,
                         "Reason": f"Captcha failed"})


        @app.route('/api/v1/promoter/pending/', methods=['GET'])
        def subvid345435():
            return ("beta")


        @app.route('/betacaptcha', methods=['GET'])
        def get456345dai456lytasks():
            return send_from_directory('', 'betacaptcha.html')


        # Get transactions
        @app.route('/api/v1/wallet/transactions/<user>', methods=['GET'])
        def getcoolbuxwalletrans(user):
            try:
                e = open(f"Database\\Wallet\\{user}", "r").read()
            except Exception:
                return ({"Success": False,
                         "Reason": f"Oops! You don't own a CoolBux wallet."})
            else:
                atrans = open(f"Database\\Wallet\\Transactions\\{user}", "r").read()
                return ({"Success": True,
                         "Transactions": f"{atrans}"})


        # Send Crypto to other people
        @app.route('/api/v1/send/<user>/<towallet>/<amount>/<sepin>/<coin>/<priority>', methods=['GET'])
        def sendcoolbuxwalletsoto(user, towallet, amount, sepin, coin, priority):

            try:
                e = open(f"Database\\Wallet\\{user}", "r").read()
            except Exception:
                return ({"Success": False,
                         "Reason": f"Oops! You don't own a CoolBux wallet."})
            else:

                print("validating pin")
                try:
                    pin = open(f"Database\\Security\\Done\\{user}", "r").read()
                except Exception:
                    return ({"Success": False,
                             "Reason": f"Oops! You need to setup a pin."})
                if sepin != pin:
                    return ({"Success": False,
                             "Reason": f"Oops! Your pin {sepin} is invalid."})
                else:
                    print("Performing balance check")

                    print("Checking coin")
                    if coin == "bitcoin":

                        BTCWif = open(f"Database\\Wallet\\BTC\\{user}", "r").read().split("*")[1]
                        print(f"({user}) -> Sending ${amount} with BTC WIF {BTCWif}")
                        print("Converting priority to USD")
                        if priority == 3:
                            insurance = 0.10
                            jsoninfo = json.loads(requests.get(
                                "https://api.coinstats.app/public/v1/coins?skip=0&limit=1").text)
                            satprice = float(jsoninfo["coins"][0]["price"]) / 100000000
                            feeprice = int(float(insurance / satprice))
                            if feeprice < 80:
                                print("Disabled BTC Payouts, fees too high")
                                return ({"Success": False,
                                         "Reason": "Bitcoin fees are too high for this option! You can choose a higher priority, or convert your Bitcoin to Litecoin."})
                        elif priority == 2:
                            insurance = 0.25
                            jsoninfo = json.loads(requests.get(
                                "https://api.coinstats.app/public/v1/coins?skip=0&limit=1").text)
                            satprice = float(jsoninfo["coins"][0]["price"]) / 100000000
                            feeprice = int(float(insurance / satprice))
                            if feeprice < 275:
                                print("Disabled BTC Payouts, fees too high")
                                return ({"Success": False,
                                         "Reason": "Bitcoin fees are too high for this option! You can choose a higher priority, or convert your Bitcoin to Litecoin."})
                        elif priority == 1:
                            insurance = 0.80
                            jsoninfo = json.loads(requests.get(
                                "https://api.coinstats.app/public/v1/coins?skip=0&limit=1").text)
                            satprice = float(jsoninfo["coins"][0]["price"]) / 100000000
                            feeprice = int(float(insurance / satprice))
                            if feeprice < 1000:
                                print("Disabled BTC Payouts, fees too high")
                                return ({"Success": False,
                                         "Reason": "Bitcoin fees are too high for this option! You can choose a higher priority, or convert your Bitcoin to Litecoin."})
                        elif priority == 0:
                            insurance = 3
                            jsoninfo = json.loads(requests.get(
                                "https://api.coinstats.app/public/v1/coins?skip=0&limit=1").text)
                            satprice = float(jsoninfo["coins"][0]["price"]) / 100000000
                            feeprice = int(float(insurance / satprice))
                            if feeprice < 3500:
                                print("Disabled BTC Payouts, fees too high")
                                return ({"Success": False,
                                         "Reason": "Bitcoin fees are too high for this option! You can choose a higher priority, or convert your Bitcoin to Litecoin."})
                        else:
                            return ({"Success": False,
                                     "Reason": f"Oops! You've sent an invalid priority."})

                        if float(amount) < 1:
                            jfy = {"Success": False,
                                   "Reason": f"The minimum withdrawl amount for Bitcoin is $1 USD"}
                            return (jsonify(jfy))
                        crpayout = str(float(amount) - insurance)
                        usr = user
                        wallet = towallet
                        # MAKE A CHECK FOR BALANCE
                        if float(amount) > float(open(f"Database\\Wallet\\Balance\\{user}", "r").read()):
                            jfy = {"Success": False,
                                   "Reason": f"You're trying to withdraw more USD than you have!"}
                            return (jsonify(jfy))
                        if float(open(f"Database\\Wallet\\Balance\\{user}", "r").read()) < 0:
                            jfy = {"Success": False,
                                   "Reason": f"Your balance is negative!"}
                            return (jsonify(jfy))

                        print("vuln integrity check")
                        if str(open(f"Database\\Wallet\\Balance\\{user}", "r").read()).__contains__("-"):
                            print(f"failed integrity check! {user} - {amount}")
                            jfy = {"Success": False,
                                   "Reason": f"Failed integrity check!"}
                            return (jsonify(jfy))

                        print(
                            f"Calculated appropiate fee | Insurance set at ${insurance} USD | ~EST {str(feeprice)} Sats (SAT Price {satprice})")
                        pres = PayBTC(crpayout, feeprice, str(wallet))
                        if pres.split(":")[1] != "ABLOL":
                            print("deducting balance...")
                            cbal = int(float(amount))
                            twe = str(amount)
                            print("getting balance")
                            balance = float(open(f'Database\\Wallet\\Balance\\{usr}', 'r').read())
                            print("got balance calculating aftermath of reducted balance")
                            afterbal = balance - cbal
                            print(afterbal)
                            df = str(afterbal)
                            print(".. setting balance ..")
                            wtp = open(f'Database\\Wallet\\Balance\\{usr}', 'w')
                            wtp.write(df)
                            iconauth = open(f"Database\\Headshots\\{usr}", "r").read()
                            lnk = str(pres).split(":")[1]

                            # Add to their history
                            userhistory = open(f"Database\\History\\{usr}", "a")
                            userhistory.write(
                                f"Successfully paid out ${crpayout} USD + $0.10 Reward In Bitcoin. (Transaction: https://mempool.space/tx/{lnk})\n")
                            userhistory.close()
                            # Log in crypto withdrawls

                            now = datetime.datetime.now()

                            print("now =", now)

                            # dd/mm/YY H:M:S
                            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                            crpd = open(f"Database\\Crypto\\withdrawls.txt", "a")
                            crpd.write(
                                f"Action taken place on {str(dt_string)} | (BTC PAYOUT) ${crpayout} USD | To wallet: {wallet} | Sent to: {usr} | Transaction: https://mempool.space/tx/{lnk} | TXID: {lnk} | Calculated Fee: {feeprice} SATS\n")
                            crpd.close()

                            requests.post(
                                "https://ptb.discord.com/api/webhooks/830622834015469595/aLHQ02sCOyFhlcJ0Tz3PoDei2YLqHWIorUg0BzJGQeEodc8sFiM8lR0wvVw4WeDXQBet",
                                json={
                                    "embeds": [
                                        {
                                            "title": f"Paid **{usr}**!",
                                            "description": f"**{usr}** Just paid out **${crpayout} USD** <:Bitcoin:863086469191434241>  **[Transaction Link](https://mempool.space/tx/{lnk})** (From CoolBux wallet)",
                                            "color": 8519030,
                                            "author": {
                                                "name": f"{usr}",
                                                "icon_url": iconauth
                                            },
                                            "footer": {
                                                "text": f"Earn BITCOIN/LITECOIN & ROBUX NOW at https://www.coolbux.live like {usr} just did!"
                                            }
                                        }
                                    ]
                                })
                            print("Appending to transactions")
                            e = open(f"Database\\Wallet\\Transactions\\{user}", "a")
                            e.write(
                                f"\n[Bitcoin Transaction] > Sent ${crpayout} USD to {wallet} with a fee of ${insurance} USD ({feeprice} Satoshis at time of sending) | Transaction: {lnk} | Transaction Link: https://mempool.space/tx/{lnk} | Taken place on {str(dt_string)}")
                            e.close()

                            return ({"Paid": True,
                                     "Reason": f"You've successfully paid ${crpayout} USD (Real Money) to the wallet {wallet}!",
                                     "Transaction": f"https://mempool.space/tx/{lnk}",
                                     "Fee": f"{feeprice}",
                                     "SatPrice": f"{satprice}"})
                        else:
                            return ({"Paid": False,
                                     "Reason": f"CoolBux payments are currently under maitenance. Try again in 1-24 hours."})


        # Get coolbux user wallet ltc address
        @app.route('/api/v1/litecoin/address/<user>', methods=['GET'])
        def ltcaddr(user):
            try:
                e = open(f"Database\\Wallet\\{user}", "r").read()
            except Exception:
                return ({"Success": False,
                         "Reason": f"Oops! You don't own a CoolBux wallet."})
            else:
                ltcinfo = open(f"Database\\Wallet\\LTC\\{user}", "r").read().split("*")[0]
                return ({"Success": True,
                         "Address": f"{ltcinfo}"})


        # Get coolbux user wallet btc address
        @app.route('/api/v1/bitcoin/address/<user>', methods=['GET'])
        def btcaddr(user):
            try:
                e = open(f"Database\\Wallet\\{user}", "r").read()
            except Exception:
                return ({"Success": False,
                         "Reason": f"Oops! You don't own a CoolBux wallet."})
            else:
                ltcinfo = open(f"Database\\Wallet\\BTC\\{user}", "r").read().split("*")[0]
                return ({"Success": True,
                         "Address": f"{ltcinfo}"})


        # check user pin if valid (made for coolbux & coolbuxshop)
        @app.route(f'/api/v1/private/pin/check/<user>/<sepin>', methods=['GET'])
        def checkpdfghin(user, sepin):
            try:
                pin = open(f"Database\\Security\\Done\\{user}", "r").read()
            except Exception:
                return ({"Valid": False,
                         "Reason": f"Oops! You need to setup a pin."})
            if sepin != pin:
                return ({"Valid": False,
                         "Reason": f"Oops! Your pin {sepin} is invalid."})
            else:
                return ({"Valid": True,
                         "Reason": f"VPin"})


        # check user pin if valid (made for coolbux & coolbuxshop)
        @app.route(f'/api/v1/pin/check/<user>/<sepin>', methods=['GET'])
        def checkpin(user, sepin):
            try:
                e = open(f"Ratelimit\\Pins\\{user}")
            except Exception as er:
                print("wto file | without")
                e = open(f"Ratelimit\\Pins\\{user}", "w")
                start_time = str(time.time())
                e.write(start_time)
                e.close()
                print(f"validating pin ({er}) | {start_time}")
                try:
                    pin = open(f"Database\\Security\\Done\\{user}", "r").read()
                except Exception:
                    return ({"Valid": False,
                             "Reason": f"Oops! You need to setup a pin."})
                if sepin != pin:
                    return ({"Valid": False,
                             "Reason": f"Oops! Your pin {sepin} is invalid."})
                else:
                    return ({"Valid": True,
                             "Reason": f"VPin"})
            else:
                print("Checking time since last request")
                vtime = float(open(f"Ratelimit\\Pins\\{user}", "r").read())
                print(vtime)
                ctime = time.time()
                print(ctime)
                rtime = ctime - vtime
                if rtime > 1:
                    print(rtime)
                    print(f"wto file ({1 - rtime} ({rtime - 1}) secs remaining)")
                    e = open(f"Ratelimit\\Pins\\{user}", "w")
                    start_time = str(time.time())
                    e.write(start_time)
                    e.close()
                    print("validating pin")
                    try:
                        pin = open(f"Database\\Security\\Done\\{user}", "r").read()
                    except Exception:
                        return ({"Valid": False,
                                 "Reason": f"Oops! You need to setup a pin."})
                    if sepin != pin:
                        return ({"Valid": False,
                                 "Reason": f"Oops! Your pin {sepin} is invalid."})
                    else:
                        return ({"Valid": True,
                                 "Reason": f"VPin"})
                else:
                    return ({"Valid": False,
                             "Reason": f"Please try again within {8 - int(rtime)} seconds."})


        # Donate from user to another user (coolbux shop feature)
        @app.route('/api/v1/donate/<orguser>/<orgpin>/<touser>/<amount>', methods=['GET'])
        def donatetouserapi(orguser, orgpin, touser, amount):
            print("validating pin")
            try:
                ogrpin2 = open(f"Database\\Security\\Done\\{orguser}", "r").read()
            except Exception:
                return ({"Donated": False,
                         "Reason": f"Oops! You need to setup a pin."})
            if orgpin != ogrpin2:
                return ({"Donated": False,
                         "Reason": f"Oops! Your pin {orgpin} is invalid."})
            else:
                print("Valid pin! Validating if Recipient is correct")
                try:
                    bmt = open(f"Database\\Pays\\{touser}", "r").read()
                except Exception:
                    return ({"Donated": False,
                             "Reason": f"Oops! It seems you aren't a registered user. Try re-logging in or using a different device."})
                else:
                    print("checking if user is banned")
                    try:
                        bmt = open(f"Database\\Banned\\{touser}", "r").read()
                    except Exception:
                        print("pass")
                        # do a balance check to see if orguser can donate
                        orgbalance = float(open(f"Database\\Pays\\{orguser}", "r").read())
                        if float(amount) > orgbalance:
                            return ({"Donated": False,
                                     "Reason": f"Oops! Please lower your payout amount. (Max Payout: {orgbalance})"})
                        else:
                            print("min payout check")
                            if float(amount) < 0.01:
                                return ({"Donated": False,
                                         "Reason": f"Oops! The minimum payout is R$0.01"})
                            else:
                                # can donate

                                now = datetime.datetime.now()
                                print("now =", now)
                                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                                e = open("donatelogs.bin", "a")
                                e.write(f"{orguser} is donating {amount} > {touser}\n")
                                e.close()

                                # Add to recep history
                                userhistory = open(f"Database\\History\\{touser}", "a")
                                userhistory.write(
                                    f"Received payment of R${amount}  from CoolBuxShop (Received on {str(dt_string)})\n")
                                userhistory.close()

                                # Add to coolbuxshop history
                                userhistory = open(f"Database\\History\\{orguser}", "a")
                                userhistory.write(
                                    f"Sent R${amount} - CoolBuxShop Payment (Sent on {str(dt_string)})\n")
                                userhistory.close()

                                # reduce balance
                                rdbalance = float(orgbalance - float(amount))
                                ovrbal = open(f"Database\\Pays\\{orguser}", "w")
                                ovrbal.write(str(rdbalance))
                                ovrbal.close()

                                # add to user
                                usrbalance = float(open(f"Database\\Pays\\{touser}", "r").read())
                                rdbalance = float(usrbalance + float(amount))
                                ovrbal = open(f"Database\\Pays\\{touser}", "w")
                                ovrbal.write(str(rdbalance))
                                ovrbal.close()

                                return ({"Donated": True,
                                         "Reason": f"Successfully recieved payment of R${amount}"})


                    else:
                        return ({"Donated": False,
                                 "Reason": f"Oops! This recipient is banned."})


        # bet feature (gamble.coolbux shop feature)
        @app.route('/api/v1/donate/gamble/<orguser>/<orgpin>/<touser>/<amount>', methods=['GET'])
        def donatetouserapibet(orguser, orgpin, touser, amount):
            print("validating pin")
            try:
                ogrpin2 = open(f"Database\\Security\\Done\\{orguser}", "r").read()
            except Exception:
                return ({"Donated": False,
                         "Reason": f"Oops! You need to setup a pin."})
            if orgpin != ogrpin2:
                return ({"Donated": False,
                         "Reason": f"Oops! Your pin {orgpin} is invalid."})
            else:
                print("Valid pin! Validating if Recipient is correct")
                try:
                    bmt = open(f"Database\\Pays\\{touser}", "r").read()
                except Exception:
                    return ({"Donated": False,
                             "Reason": f"Oops! It seems you aren't a registered user. Try re-logging in or using a different device."})
                else:
                    print("checking if user is banned")
                    try:
                        bmt = open(f"Database\\Banned\\{touser}", "r").read()
                    except Exception:
                        print("pass")
                        # do a balance check to see if orguser can donate
                        orgbalance = float(open(f"Database\\Pays\\{orguser}", "r").read())
                        if float(amount) > orgbalance:
                            return ({"Donated": False,
                                     "Reason": f"Oops! Please lower your amount. (Max: {orgbalance})"})
                        else:
                            print("min payout check")
                            if float(amount) < 1:
                                return ({"Donated": False,
                                         "Reason": f"Oops! The minimum amount is R$1"})
                            else:
                                # can donate

                                # reduce balance
                                rdbalance = float(orgbalance - float(amount))
                                ovrbal = open(f"Database\\Pays\\{orguser}", "w")
                                ovrbal.write(str(rdbalance))
                                ovrbal.close()

                                # add to user
                                usrbalance = float(open(f"Database\\Pays\\{touser}", "r").read())
                                rdbalance = float(usrbalance + float(amount))
                                ovrbal = open(f"Database\\Pays\\{touser}", "w")
                                ovrbal.write(str(rdbalance))
                                ovrbal.close()

                                now = datetime.datetime.now()
                                print("now =", now)
                                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                                usdamt = float(amount) * 0.005

                                # Add to recep history
                                userhistory = open(f"Database\\History\\{touser}", "a")
                                userhistory.write(
                                    f"Received R${amount} (${usdamt} USD) from winning a bet (Received on {str(dt_string)})\n")
                                userhistory.close()

                                # Add to coolbuxshop history
                                userhistory = open(f"Database\\History\\{orguser}", "a")
                                userhistory.write(
                                    f"Sent R${amount} (${usdamt} USD)- Gambling Payment (Sent on {str(dt_string)})\n")
                                userhistory.close()

                                return ({"Donated": True,
                                         "Reason": f"Successfully recieved payment of R${amount}"})


                    else:
                        return ({"Donated": False,
                                 "Reason": f"Oops! This recipient is banned."})


        # Create CoolBux wallet
        @app.route('/api/v1/create/wallet/<user>/<sepin>', methods=['GET'])
        def crwallet(user, sepin):
            print(f"Creating CoolBux wallet under {user}")
            # Check if they're registered
            try:
                bmt = open(f"Database\\Pays\\{user}", "r").read()
            except Exception:
                return ({"Created": False,
                         "Reason": f"Oops! It seems you aren't a registered user. Try re-logging in or using a different device."})
            else:
                print("User valid! Checking if eligible to create")
                if float(bmt) < 1:
                    return ({"Created": False,
                             "Reason": f"Oops! You need a minimum of 1 robux to create a CoolBux wallet."})
                else:
                    print("checking if already created wallet")
                    try:
                        e = open(f"Database\\Wallet\\{user}", "r").read()
                    except Exception:
                        print("validating pin")
                        try:
                            pin = open(f"Database\\Security\\Done\\{user}", "r").read()
                        except Exception:
                            return ({"Created": False,
                                     "Reason": f"Oops! You need to setup a pin."})
                        if sepin != pin:
                            return ({"Created": False,
                                     "Reason": f"Oops! Your pin {sepin} is invalid."})

                        print("Creating wallet!")
                        # Create Bitcoin address to get payments
                        key = Key()
                        wifkey = str(key.to_wif).split(": ")[1].strip(">>")
                        segaddr = str(key.segwit_address)
                        e = open(f"Database\\Wallet\\BTC\\{user}", "w")
                        e.write(f"{segaddr}*{wifkey}")
                        e.close()

                        # Create litecoin address to get payments
                        ltcwlt = GetLTCWallet()
                        e = open(f"Database\\Wallet\\LTC\\{user}", "w")
                        addr = ltcwlt.split("*")[0]
                        wif = ltcwlt.split("*")[1]
                        e.write(f"{addr}*{wif}")
                        e.close()

                        # Create transactions
                        e = open(f"Database\\Wallet\\Transactions\\{user}", "w")
                        e.write("")
                        e.close()

                        # Create main-balance system
                        e = open(f"Database\\Wallet\\Balance\\{user}", "w")
                        e.write("0")
                        e.close()

                        return ({"Created": True,
                                 "Reason": f"Wallet has been created"})
                    else:
                        return ({"Created": False,
                                 "Reason": f"Oops! You've already created a wallet"})


        # Create CoolBux Chat
        @app.route('/api/v1/create/chat/<user>/<seller>/<product>', methods=['GET'])
        def crchat(user, seller, product):
            chatid = str(secrets.token_hex(12))

            # create chats on users
            achats = open(f"Database\\Chats\\Open\\{user}", "a")
            achats.write(f"{product}*{seller}*{chatid}\n")
            achats.close()
            # on seller
            achats = open(f"Database\\Chats\\Open\\{seller}", "a")
            achats.write(f"{product}*{user}*{chatid}\n")
            achats.close()

            e = open(f"Database\\Chats\\{chatid}", "w")
            e.write(f"1*{user}*{seller}*{product}")
            e.close()
            e = open(f"Database\\Chats\\Info\\{chatid}", "w")
            e.write(f"{user}*{seller}")
            e.close()
            return ({"Created": True,
                     "ChatID": str(chatid),
                     "Reason": f"Created chat with {seller} & {user}"})


        # Send message to chat
        @app.route('/api/v1/chat/<id>/<user>/<message>', methods=['GET'])
        def sendchat(id, user, message):
            print("checking rate limit")
            try:
                e = open(f"Ratelimit\\Chat\\{user}")
            except Exception as er:
                e = open(f"Ratelimit\\Chat\\{user}", "w")
                start_time = str(time.time())
                e.write(start_time)
                e.close()
                print("checking if chat exists")

                chatid = id
                try:
                    e = open(f"Database\\Chats\\Info\\{id}", "r").read().split("*")
                except Exception:
                    return ({"Sent": False,
                             "Reason": f"This chat doesn't exist! It may have been deleted by a Moderator."})
                else:
                    print("chat exists! checking if user in it")
                    print(e)
                    u1 = e[0]
                    u2 = e[1]
                    if user == u2:
                        print("seller")
                        e = open(f"Database\\Chats\\{chatid}", "a")
                        e.write(f"\nseller*{u2}*{message}\n")
                        e.close()
                        print(f"Sent {message} as seller")
                        jfy = {"Success": True,
                               "Reason": f"Sent Message"}
                        return (jsonify(jfy))
                    elif user == u1:
                        print("buyer")
                        e = open(f"Database\\Chats\\{chatid}", "a")
                        e.write(f"\nbuyer*{u1}*{message}\n")
                        e.close()
                        print(f"Sent {message} as buyer")
                        jfy = {"Success": True,
                               "Reason": f"Sent Message"}
                        return (jsonify(jfy))
            else:
                print("Checking time since last request")
                vtime = float(open(f"Ratelimit\\Chat\\{user}", "r").read())
                print(vtime)
                ctime = time.time()
                print(ctime)
                rtime = ctime - vtime
                if rtime > 5:
                    print("checking if chat exists")
                    chatid = id
                    try:
                        e = open(f"Database\\Chats\\Info\\{id}", "r").read().split("*")
                    except Exception:
                        return ({"Sent": False,
                                 "Reason": f"This chat doesn't exist! It may have been deleted by a Moderator."})
                    else:
                        print("chat exists! checking if user in it")
                        print(e)
                        u1 = e[0]
                        u2 = e[1]
                        if user == u2:
                            print("seller")
                            e = open(f"Database\\Chats\\{chatid}", "a")
                            e.write(f"\nseller*{u2}*{message}\n")
                            e.close()
                            print(f"Sent {message} as seller")
                            jfy = {"Success": True,
                                   "Reason": f"Sent Message"}
                            return (jsonify(jfy))
                        elif user == u1:
                            print("buyer")
                            e = open(f"Database\\Chats\\{chatid}", "a")
                            e.write(f"\nbuyer*{u1}*{message}\n")
                            e.close()
                            print(f"Sent {message} as buyer")
                            jfy = {"Success": True,
                                   "Reason": f"Sent Message"}
                            return (jsonify(jfy))
                else:
                    jfy = {"Success": False,
                           "Reason": f"Please wait 5 seconds before sending another message"}
                    return (jsonify(jfy))


        # View chat
        @app.route('/api/v1/chat/view/<id>/<user>', methods=['GET'])
        def viewchat(id, user):
            wto = open(f"Database\\Chats\\Online\\{user}", "w")
            start_time = str(time.time())
            wto.write(start_time)
            wto.close()
            try:
                open(f"Database\\Chats\\{id}", "r").read()
            except Exception:
                jfy = {"Success": False,
                       "Reason": f"This chat doesn't exist! It may have been deleted by a Moderator."}
                return (jsonify(jfy))
            else:
                print("checking if username is part of conversation")
                e = open(f"Database\\Chats\\Info\\{id}", "r").read().split("*")
                u1 = e[0]
                u2 = e[1]
                if user == u2:
                    print("seller")
                    print("checking if buyer online or not..")
                    try:
                        open(f"Database\\Chats\\Online\\{u1}", "r").read()
                    except Exception:
                        return (jsonify({"Success": True,
                                         "Chat": open(f"Database\\Chats\\{id}", "r").read(),
                                         "BuyerOnline": False,
                                         "SellerOnline": True}))
                    vtime = float(open(f"Database\\Chats\\Online\\{u1}", "r").read())
                    print(vtime)
                    ctime = time.time()
                    print(ctime)
                    rtime = ctime - vtime
                    if rtime > 60:
                        return (jsonify({"Success": True,
                                         "Chat": open(f"Database\\Chats\\{id}", "r").read(),
                                         "BuyerOnline": False,
                                         "SellerOnline": True}))
                    else:
                        return (jsonify({"Success": True,
                                         "Chat": open(f"Database\\Chats\\{id}", "r").read(),
                                         "BuyerOnline": True,
                                         "SellerOnline": True}))


                elif user == u1:
                    print("user")
                    print("checking if seller online or not..")
                    try:
                        open(f"Database\\Chats\\Online\\{u2}", "r").read()
                    except Exception:
                        return (jsonify({"Success": True,
                                         "Chat": open(f"Database\\Chats\\{id}", "r").read(),
                                         "BuyerOnline": True,
                                         "SellerOnline": False}))
                    vtime = float(open(f"Database\\Chats\\Online\\{u2}", "r").read())
                    print(vtime)
                    ctime = time.time()
                    print(ctime)
                    rtime = ctime - vtime
                    if rtime > 60:
                        return (jsonify({"Success": True,
                                         "Chat": open(f"Database\\Chats\\{id}", "r").read(),
                                         "BuyerOnline": True,
                                         "SellerOnline": False}))
                    else:
                        return (jsonify({"Success": True,
                                         "Chat": open(f"Database\\Chats\\{id}", "r").read(),
                                         "BuyerOnline": True,
                                         "SellerOnline": True}))
                else:
                    return (jsonify({"Success": False,
                                     "Reason": "You aren't part of this conversation!"}))


        # View user chats
        @app.route('/api/v1/user/chats/<user>', methods=['GET'])
        def viewchatoffuser(user):
            try:
                achats = open(f"Database\\Chats\\Open\\{user}", "r").read()
            except Exception:
                return (jsonify({"Success": True,
                                 "Chats": f"We couldn't find any chats associated with you :("}))
            else:
                return (jsonify({"Success": True,
                                 "Chats": achats}))


        # toy info api
        @app.route('/api/v1/purchase/toy/<id>', methods=['GET'])
        def toyinfo(id):
            try:
                toyinfo = open(f"Database\\Toys\\Redeem\\{id}").read()
            except Exception:
                return (jsonify({"Success": False,
                                 "Reason": "This code doesn't exist"}))
            else:
                return (jsonify({"Success": True,
                                 "Reason": toyinfo}))


        # purchase toy
        @app.route('/api/v1/purchase/toy/<user>/<pin>', methods=['GET'])
        def buytoyc2345de(user, pin):
            print("checking if toy codes in stock")
            toystock = open(f"Database\\GiftCards\\toys.bin", "r").read().split("\n")
            toysav = 0
            for toy in toystock:
                toysav += 1
            totaltoys = toysav - 1
            if totaltoys < 1:
                return (jsonify({"Success": False,
                                 "Reason": "Oops! There currently isn't any toys in stock."}))
            else:
                print("== Toys in stock, doing integrity checks ==")
                # Start integirty checks
                print("testing if user exists")
                try:
                    e = open('Database\\Pays\\' + user, 'r')
                    e.read()
                except Exception:
                    print('user doesnt exist')
                    jfy = {"Paid": False,
                           "Reason": "User doesn't exist"}
                    return (jsonify(jfy))
                else:
                    print("checking if balance negative")
                    balance = int(float(open(f'Database\\Pays\\{user}', 'r').read()))
                    if balance < 0:
                        print("bad balance")
                        jfy = {"Paid": False,
                               "Reason": "Your balance is negative!"}
                        return (jsonify(jfy))


                    else:
                        print("check if user has minimum / over amount")
                        balance = int(float(open(f'Database\\Pays\\{user}', 'r').read()))
                        if balance < 50:
                            print("under minimum")
                            jfy = {"Paid": False,
                                   "Reason": "Minimum amount to payout toys is 50 robux."}
                            return (jsonify(jfy))

                        else:
                            print("checking balance")
                            balance = int(float(open(f'Database\\Pays\\{user}', 'r').read()))
                            if 50 > balance:
                                print("not enough")
                                jfy = {"Paid": False,
                                       "Reason": "You don't have enough robux to payout this amount! 50 Robux is required to get a toy."}
                                return (jsonify(jfy))
                            else:
                                try:
                                    sepin = open(f"Database\\Security\\Done\\{user}", "r").read()
                                except Exception:
                                    return ({"Paid": False,
                                             "Reason": f"Oops! You need to setup a pin."})
                                if pin != sepin:
                                    return ({"Paid": False,
                                             "Reason": f"Oops! Your pin {sepin} is invalid."})
                                else:
                                    toycode = None
                                    # get a toy code for the user
                                    if totaltoys == 0:
                                        toycode = open(f"Database\\GiftCards\\toys.bin").read().strip("\n")

                                    with open(r"Database\\GiftCards\\toys.bin", 'r+') as fp:
                                        lines = fp.readlines()
                                        fp.seek(0)
                                        fp.truncate()
                                        toycode = lines[1]
                                        fp.writelines(lines[1:])
                                    print(f"got toycode: {toycode}")
                                    if toycode == None:
                                        return ({"Paid": False,
                                                 "Reason": f"Oops! There currently isn't any toycodes in stock."})
                                    else:
                                        # remove their balance
                                        balance = float(open(f'Database\\Pays\\{user}', 'r').read())
                                        afterbal = balance - 50
                                        df = str(afterbal)
                                        wtp = open(f'Database\\Pays\\{user}', 'w')
                                        wtp.write(df)
                                        wtp.close()

                                        # now get coolbux asoc id to get toy information to give user
                                        asocid = toycode.split("*")[1].strip("\n")
                                        jsonasoc = json.loads(open(f"Database\\GiftCards\\toyinfo.json").read())
                                        toyname = jsonasoc[f"{asocid}-name"]
                                        toyimg = jsonasoc[f"{asocid}-image"]
                                        toylink = jsonasoc[f"{asocid}-link"]
                                        rtoycode = toycode.strip("*")[0]

                                        # generate link code for toy
                                        rtoylkcode = str(secrets.token_hex(18).lower())
                                        e = open(f"Database\\Toys\\Redeem\\{rtoylkcode}", "w")
                                        e.write(
                                            f"Your toy code is {rtoycode} \n You will recieve the item {toyname} upon redemtion. This can only be redeemed once!")
                                        e.close()

                                        userhistory = open(f"Database\\History\\{user}", "a")
                                        userhistory.write(
                                            f"Successfully recieved Toy Code for R$50 (Link: coolbux.live/toys/code/{rtoylkcode})\n")
                                        userhistory.close()
                                        iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                                        requests.post(
                                            "https://ptb.discord.com/api/webhooks/830622834015469595/aLHQ02sCOyFhlcJ0Tz3PoDei2YLqHWIorUg0BzJGQeEodc8sFiM8lR0wvVw4WeDXQBet",
                                            json={
                                                "embeds": [
                                                    {
                                                        "title": f"Paid **{user}**!",
                                                        "description": f"**{user}** Just claimed a **Roblox Virtual Item!** for **R$50**",
                                                        "color": 8519030,
                                                        "author": {
                                                            "name": f"{user}",
                                                            "icon_url": iconauth
                                                        },
                                                        "footer": {
                                                            "text": f"Earn robux NOW at https://www.coolbux.live like {user} did!"
                                                        }
                                                    }
                                                ]
                                            })
                                        return ({
                                            "Success": True,
                                            "Image": toyimg,
                                            "Code": rtoycode,
                                            "Link": toylink,
                                            "ToyName": toyname
                                        })


        # purchase giftcard
        @app.route('/api/v1/purchase/giftcard/<user>/<pin>', methods=['GET'])
        def buygccardcode(user, pin):
            print("checking if toy codes in stock")
            toystock = open(f"Database\\GiftCards\\gcs.bin", "r").read().split("\n")
            toysav = 0
            for toy in toystock:
                toysav += 1
            totaltoys = toysav - 1
            if totaltoys < 1:
                return (jsonify({"Success": False,
                                 "Reason": "Oops! There currently isn't any giftcards in stock."}))
            else:
                print("== Toys in stock, doing integrity checks ==")
                # Start integirty checks
                print("testing if user exists")
                try:
                    e = open('Database\\Pays\\' + user, 'r')
                    e.read()
                except Exception:
                    print('user doesnt exist')
                    jfy = {"Paid": False,
                           "Reason": "User doesn't exist"}
                    return (jsonify(jfy))
                else:
                    print("checking if balance negative")
                    balance = int(float(open(f'Database\\Pays\\{user}', 'r').read()))
                    if balance < 0:
                        print("bad balance")
                        jfy = {"Paid": False,
                               "Reason": "Your balance is negative!"}
                        return (jsonify(jfy))


                    else:
                        print("check if user has minimum / over amount")
                        balance = int(float(open(f'Database\\Pays\\{user}', 'r').read()))
                        if balance < 1000:
                            print("under minimum")
                            jfy = {"Paid": False,
                                   "Reason": "Minimum amount to payout giftcards is 1000 robux."}
                            return (jsonify(jfy))

                        else:
                            print("checking balance")
                            balance = int(float(open(f'Database\\Pays\\{user}', 'r').read()))
                            if 1000 > balance:
                                print("not enough")
                                jfy = {"Paid": False,
                                       "Reason": "You don't have enough robux to payout this amount! 1000 Robux is required to get a giftcard."}
                                return (jsonify(jfy))
                            else:
                                try:
                                    sepin = open(f"Database\\Security\\Done\\{user}", "r").read()
                                except Exception:
                                    return ({"Paid": False,
                                             "Reason": f"Oops! You need to setup a pin."})
                                if pin != sepin:
                                    return ({"Paid": False,
                                             "Reason": f"Oops! Your pin {sepin} is invalid."})
                                else:
                                    toycode = None
                                    # get a toy code for the user
                                    if totaltoys == 0:
                                        toycode = open(f"Database\\GiftCards\\gcs.bin").read().strip("\n")

                                    with open(r"Database\\GiftCards\\gcs.bin", 'r+') as fp:
                                        lines = fp.readlines()
                                        fp.seek(0)
                                        fp.truncate()
                                        toycode = lines[1]
                                        fp.writelines(lines[1:])
                                    print(f"got gc: {toycode}")
                                    if toycode == None:
                                        return ({"Paid": False,
                                                 "Reason": f"Oops! There currently isn't any giftcards in stock."})
                                    else:
                                        # remove their balance
                                        balance = float(open(f'Database\\Pays\\{user}', 'r').read())
                                        afterbal = balance - 1000
                                        df = str(afterbal)
                                        wtp = open(f'Database\\Pays\\{user}', 'w')
                                        wtp.write(df)
                                        wtp.close()

                                        userhistory = open(f"Database\\History\\{user}", "a")
                                        userhistory.write(
                                            f"Successfully bought Giftcard for R$1,000\n")
                                        userhistory.close()
                                        iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                                        requests.post(
                                            "https://ptb.discord.com/api/webhooks/830622834015469595/aLHQ02sCOyFhlcJ0Tz3PoDei2YLqHWIorUg0BzJGQeEodc8sFiM8lR0wvVw4WeDXQBet",
                                            json={
                                                "embeds": [
                                                    {
                                                        "title": f"Paid **{user}**!",
                                                        "description": f"**{user}** Just claimed a **Giftcard** for **R$1,000**",
                                                        "color": 8519030,
                                                        "author": {
                                                            "name": f"{user}",
                                                            "icon_url": iconauth
                                                        },
                                                        "footer": {
                                                            "text": f"Earn robux NOW at https://www.coolbux.live like {user} did!"
                                                        }
                                                    }
                                                ]
                                            })
                                        return ({"Success": True,
                                                 "Code": toycode})


        # purchase giftcard
        @app.route('/api/v1/purchase/giftcard/<user>/<pin>', methods=['GET'])
        def buytoycode(user, pin):
            print("checking if toy codes in stock")
            toystock = open(f"Database\\GiftCards\\gcs.bin", "r").read().split("\n")
            toysav = 0
            for toy in toystock:
                toysav += 1
            totaltoys = toysav - 1
            if totaltoys < 1:
                return (jsonify({"Success": False,
                                 "Reason": "Oops! There currently isn't any giftcards in stock."}))
            else:
                print("== gcs in stock, doing integrity checks ==")
                # Start integirty checks
                print("testing if user exists")
                try:
                    e = open('Database\\Pays\\' + user, 'r')
                    e.read()
                except Exception:
                    print('user doesnt exist')
                    jfy = {"Paid": False,
                           "Reason": "User doesn't exist"}
                    return (jsonify(jfy))
                else:
                    print("checking if balance negative")
                    balance = int(float(open(f'Database\\Pays\\{user}', 'r').read()))
                    if balance < 0:
                        print("bad balance")
                        jfy = {"Paid": False,
                               "Reason": "Your balance is negative!"}
                        return (jsonify(jfy))


                    else:
                        print("check if user has minimum / over amount")
                        balance = int(float(open(f'Database\\Pays\\{user}', 'r').read()))
                        if balance < 50:
                            print("under minimum")
                            jfy = {"Paid": False,
                                   "Reason": "Minimum amount to payout giftcards is 1,000 robux."}
                            return (jsonify(jfy))

                        else:
                            print("checking balance")
                            balance = int(float(open(f'Database\\Pays\\{user}', 'r').read()))
                            if 50 > balance:
                                print("not enough")
                                jfy = {"Paid": False,
                                       "Reason": "You don't have enough robux to payout this amount! 1,000 Robux is required to get a giftcard."}
                                return (jsonify(jfy))
                            else:
                                try:
                                    sepin = open(f"Database\\Security\\Done\\{user}", "r").read()
                                except Exception:
                                    return ({"Paid": False,
                                             "Reason": f"Oops! You need to setup a pin."})
                                if pin != sepin:
                                    return ({"Paid": False,
                                             "Reason": f"Oops! Your pin {sepin} is invalid."})
                                else:
                                    toycode = None
                                    # get a toy code for the user
                                    if totaltoys == 0:
                                        toycode = open(f"Database\\GiftCards\\gcs.bin").read().strip("\n")

                                    with open(r"Database\\GiftCards\\gcs.bin", 'r+') as fp:
                                        lines = fp.readlines()
                                        fp.seek(0)
                                        fp.truncate()
                                        toycode = lines[1]
                                        fp.writelines(lines[1:])
                                    print(f"got toycode: {toycode}")
                                    if toycode == None:
                                        return ({"Paid": False,
                                                 "Reason": f"Oops! There currently isn't any giftcards in stock."})
                                    else:
                                        # remove their balance
                                        balance = float(open(f'Database\\Pays\\{user}', 'r').read())
                                        afterbal = balance - 50
                                        df = str(afterbal)
                                        wtp = open(f'Database\\Pays\\{user}', 'w')
                                        wtp.write(df)
                                        wtp.close()

                                        # generate link code for toy
                                        rtoylkcode = str(secrets.token_hex(18).lower())
                                        e = open(f"Database\\Toys\\Redeem\\{rtoylkcode}", "w")
                                        e.write(
                                            f"Your giftcard code is {toycode} , redeem it at https://www.roblox.com/redeem or at roblox checkout.")
                                        e.close()

                                        userhistory = open(f"Database\\History\\{user}", "a")
                                        userhistory.write(
                                            f"Successfully bought giftcard for R$1,000 | redeem it at https://www.roblox.com/redeem or at roblox checkout.\n")
                                        userhistory.close()
                                        iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                                        requests.post(
                                            "https://ptb.discord.com/api/webhooks/830622834015469595/aLHQ02sCOyFhlcJ0Tz3PoDei2YLqHWIorUg0BzJGQeEodc8sFiM8lR0wvVw4WeDXQBet",
                                            json={
                                                "embeds": [
                                                    {
                                                        "title": f"Paid **{user}**!",
                                                        "description": f"**{user}** Just claimed a **Roblox Giftcard!** for **R$1,000**",
                                                        "color": 8519030,
                                                        "author": {
                                                            "name": f"{user}",
                                                            "icon_url": iconauth
                                                        },
                                                        "footer": {
                                                            "text": f"Earn robux NOW at https://www.coolbux.live like {user} did!"
                                                        }
                                                    }
                                                ]
                                            })
                                        return ({"Paid": True,
                                                 "GiftLink": f"https://coolbux.live/roblox/giftcard/{rtoylkcode}"})


        # createTask API
        @app.route('/api/v1/easycaptcha/createTask/<apikey>/<cost>/<capkey>', methods=['GET'])
        def createTask(apikey, cost, capkey):
            # checking api key validity
            try:
                apikeybal = open(f"Database\\EasyCaptcha\\{apikey}", "r").read()
            except Exception:
                return (jsonify({
                    "errorId": 1,
                    "errorCode": "ERROR_KEY_DOES_NOT_EXIST",
                    "errorDescription": "Account authorization key not found in the system"
                }))
            else:
                if float(apikeybal) < float(cost):
                    return (jsonify({
                        "errorId": 2,
                        "errorCode": "ERROR_INSUFFICIENT_BALANCE",
                        "errorDescription": "This ClientKey doesn't have enough balance"
                    }))
                elif float(cost) < 0.0009:
                    return (jsonify({
                        "errorId": 4,
                        "errorCode": "ERROR_UNDER_MINIMUM",
                        "errorDescription": "The minimum cost per captcha is $0.0009"
                    }))
                else:
                    # deduct balance
                    nbal = float(apikeybal) - float(cost)
                    ovr = open(f"Database\\EasyCaptcha\\{apikey}", "w")
                    ovr.write(str(nbal))
                    ovr.close()
                    # create task id
                    taskid = secrets.token_hex(16)
                    # put into queue
                    e = open("Database\\Captcha\\queue.bin", "a")
                    e.write(f"{taskid}*{cost}*{apikey}*{capkey}\n")
                    e.close()
                    # add to pending captchas
                    cepnd = int(open(f"Database\\Captcha\\CEpnd\\{apikey}", "r").read())
                    cepnd += 1
                    newpend = open(f"Database\\Captcha\\CEpnd\\{apikey}", "r")
                    newpend.write(str(cepnd))
                    newpend.close()

                    return (jsonify({
                        "errorId": 0,
                        "taskId": taskid
                    }))


        # CreateSession API (Based on priority count of captchas)
        @app.route('/api/v1/GetBestCaptcha', methods=['GET'])
        def gbestcaptcha():
            # determine count of users in queue
            mcommon = []
            tqueue = 0
            for cap in open("Database\\Captcha\\queue.bin", "r").read().split("\n"):
                if cap == "\n":
                    print("false captcha")
                else:
                    tqueue += 1
                    mcommon.append(cap.split("*")[3])
                    print("appened queue captcha")
            if tqueue == 0:
                return (jsonify({
                    "PublicKey": "Default_Key",
                    "Type": "Default_CoolBux"
                }))
            else:
                # get most prio bidder
                highestbd = [0.0009]
                for cap in open("Database\\Captcha\\queue.bin", "r").read().split("\n"):
                    if cap == "\n":
                        print("false captcha")
                    else:
                        print("[-] -> Checking if beats pre bidder (or above default)")
                        nbid = float(cap.split("*")[1])
                        tskid = cap.split("*")[0]
                        ogapikey = cap.split("*")[2]
                        type = cap.split("*")[3]
                        if nbid > 0.0009:
                            # beats default price, adding to board
                            if nbid > highestbd:
                                highestbd = nbid
                                print("applied to board")
                            else:
                                print("not appliciable for board | however adding extra entries dep on bid")
                                if nbid > 0.001:
                                    mcommon.append(type)
                                elif nbid > 0.0015:
                                    mcommon.append(type)
                                    mcommon.append(type)
                                elif nbid > 0.002:
                                    mcommon.append(type)
                                    mcommon.append(type)
                                elif nbid > 0.0025:
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                elif nbid > 0.004:
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                elif nbid > 0.005:
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                elif nbid > 0.006:
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                elif nbid > 0.007:
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                elif nbid > 0.01:
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)
                                    mcommon.append(type)

                frequency_distribution = nltk.FreqDist(mcommon)
                req_captcha = frequency_distribution.max()
                return (jsonify({
                    "PublicKey": req_captcha,
                    "Type": f"Versatile_Queue_System"
                }))


        # checkTask API
        @app.route('/api/v1/easycaptcha/getTaskResult/<key>/<taskId>', methods=['GET'])
        def getTaskResult():

            apikey = request.form.get('clientKey')
            taskId = request.form.get('taskId')
            # checking api key validity
            try:
                apikeybal = open(f"Database\\EasyCaptcha\\{apikey}", "r").read()
            except Exception:
                return (jsonify({
                    "errorId": 1,
                    "errorCode": "ERROR_KEY_DOES_NOT_EXIST",
                    "errorDescription": "Account authorization key not found in the system"
                }))
            else:
                # check if apikey in queue
                valid = False
                vcost = None
                for rtaskid in open("Database\\Captcha\\queue.bin", "r").read().split("\n"):
                    if rtaskid.split("*")[0] == taskId:
                        valid = True
                        vcost = rtaskid.split("*")[1]
                    else:
                        pass
                if valid == False:
                    return (jsonify({
                        "errorId": 3,
                        "errorCode": "ERROR_TASK_DOES_NOT_EXIST",
                        "errorDescription": "This taskId doesn't exist. This task may be old."
                    }
                    ))
                else:
                    # task valid - check if completed or refunded
                    try:
                        tasksolved = open(f"Database\\Captcha\\Completed\\{taskId}", "r").read()
                    except Exception:
                        return (jsonify({
                            "errorId": 0,
                            "status": "processing",
                            "solvedToken": None,
                            "cost": vcost,
                            "solvedBy": None
                        }
                        ))
                    else:
                        # check if refunded
                        try:
                            e = open(f"DatabaseCaptcha\\Refund\\{taskId}")
                        except Exception:
                            return (jsonify({
                                "errorId": 0,
                                "status": "refunded",
                                "solvedToken": None,
                            }
                            ))
                        else:

                            print("task solved! getting token")
                            token = tasksolved.split("*")[0]
                            return (jsonify({
                                "errorId": 0,
                                "status": "ready",
                                "solvedToken": token,
                                "cost": vcost,
                                "solvedBy": tasksolved.split("*")[1]
                            }
                            ))


        # refund API
        @app.route('/api/v1/easycaptcha/refund/<key>/<taskId>', methods=['GET'])
        def refundAPI(key):

            # make sure its within 5 min otherwise we dont refund

            apikey = request.form.get('clientKey')
            spoofTaskId = request.form.get('taskId')
            obj = AES.new('5bb91417e55d908bb700b5d7532f70d8'.encode("utf8"), AES.MODE_CBC,
                          "53d04e9d01b73566".encode("utf8"))

            try:
                rtaskid = obj.decrypt(bytes(spoofTaskId))
            except Exception:
                return (jsonify({
                    "errorId": 5,
                    "errorCode": "ERROR_ACCESS_DENIED",
                    "errorDescription": "Access has been denied"
                }))

            # check if apikey exists
            try:
                balance = open(f"Database\\Captcha\\{apikey}", "r").read()
            except Exception:
                return (jsonify({
                    "errorId": 1,
                    "errorCode": "ERROR_KEY_DOES_NOT_EXIST",
                    "errorDescription": "Account authorization key not found in the system"
                }))

            # check if task exists
            try:
                texist = open(f"Database\\Completed\\{rtaskid}", "r").read()
            except Exception:
                return (jsonify({
                    "errorId": 3,
                    "refunded": False,
                    "errorCode": "ERROR_TASK_DOES_NOT_EXIST",
                    "errorDescription": "This taskId doesn't exist / isn't completed yet."
                }
                ))
            else:
                # check time since task
                timesincetask = float(texist.split("*")[3])
                currenttime = time.time()

                if currenttime - timesincetask < 240:

                    taskPrice = texist.split("*")[2]
                    ogUsr = texist.split("*")[0]
                    trfndssc = 0

                    # check total refunds submitted
                    try:
                        trfnds = open(f"Database\\Captcha\\Refund\\{apikey}", "r").read()
                    except Exception:
                        # add to total refunds within hour (user doesn't have any as program auto removes after hour of first refund creation)
                        e = open(f"Database\\Captcha\\Refund\\{apikey}", "a")
                        e.write("{}*{}*{}".format(taskPrice, ogUsr, str(time.time())))
                        e.close()
                    else:
                        for refund in trfnds.split("\n"):
                            print(f"Counted refund | {refund}")
                            trfnds += 1
                        # compare to total captchas created within hour and compare as score
                        totalhoursolved = int(open(f"Database\\Captcha\\TSVD\\{apikey}", "r").read().split("*")[0])
                        # generate a score (closer to 0 more reliable they are, if score is above 30 refund cannot be submitted)
                        if trfndssc / totalhoursolved < 5:
                            print("quality score too low")
                            return (jsonify({
                                "errorId": 8,
                                "refunded": False,
                                "errorCode": "ERROR_QUALITY_SCORE_TOO_LOW",
                                "errorDescription": f"Your quality score is too low to submit a refund. You will be able to submit further refunds in another hour"
                            }
                            ))
                        else:
                            # process refund (log it)
                            e = open(f"Database\\Captcha\\Refund\\{apikey}", "a")
                            e.write("{}*{}*{}".format(taskPrice, ogUsr, str(time.time())))
                            e.close()
                            # add to their balance
                            cbal = float(open(f"Database\\Captcha\\{apikey}", "r").read())
                            cbal += float(taskPrice)
                            newbalance = open(f"Database\\Captcha\\{apikey}", "w")
                            newbalance.write(str(cbal))
                            newbalance.close()
                            return (jsonify({
                                "errorId": 0,
                                "refunded": True,
                                "errorDescription": f"Refund has been submitted, you've been refunded ${taskPrice} USD"
                            }
                            ))




                else:
                    return (jsonify({
                        "errorId": 7,
                        "refunded": False,
                        "errorCode": "ERROR_TIME_OVER_4_MINUTES",
                        "errorDescription": "A Refund can only be submitted at a maximum of 4 minutes after completion"
                    }
                    ))

                pass


        # keyInfo API
        @app.route('/api/v1/easycaptcha/keyInfo', methods=['POST'])
        def getusrInfo():
            usrInfo = str(request.cookies.get('.EASY-CAPTCHA-SECURITY')).split("_|")[1].strip(" ")
            print(usrInfo)
            try:
                balance = open(f"Database\\Captcha\\{usrInfo}", "r").read()
            except Exception:
                return (jsonify({
                    "errorId": 1,
                    "errorCode": "ERROR_KEY_DOES_NOT_EXIST",
                    "errorDescription": "Account authorization key not found in the system"
                }))
            else:
                # get total solved
                tslved = open(f"Database\\Captcha\\TotalSolved\\{usrInfo}", "r").read()
                # balance
                bal = open(f"Database\\Captcha\\{usrInfo}", "r").read()
                # get pending captchas
                pnding = open(f"Database\\Captcha\\CEpnd\\{usrInfo}", "r").read()
                return (jsonify({
                    "Success": True,
                    "errorId": 0,
                    "Balance": bal,
                    "totalSolved": str(tslved),
                    "pendingCaptcha": pnding
                }))


        # createKey API
        @app.route('/api/v1/easycaptcha/createAccount', methods=['POST'])
        def createAccount():
            email = request.form.get('email')
            referrer = request.form.get('ref')
            print("check email validity")
            if (re.match('\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)):
                print("checking if already registered")
                try:
                    open(f"Database\\Captcha\\Registered\\{email}", "w")
                except Exception:
                    print("valid sending verification link")
                    vtoken = str(secrets.token_hex(20) + str(random.randrange(0, 9999999999)))
                    e = open(f"Database\\Captcha\\VEmail\\{vtoken}", "w")
                    e.write(str(email) + "*" + str(referrer))
                    e.close()
                    verifylink = f"https://coolbux.live/easycaptcha/email/verification/{vtoken}"
                    result = SendMail(senderaddress="easycaptchas@gmail.com", senderpassword="Ashton2101!",
                                      reciever=email, body=f'''Hello, {str(email).split('@')[0]}.

                            Please go on this link {verifylink} to verify your email, after this go back to https://www.easycaptchas.coolbux.live/ and redeem a EasyCaptcha giftcard/deposit to begin.

                            Best Regards, 
                            - EasyCaptchas Team''', subject="EasyCaptchas Email Verification")

                    if result == "Sent":
                        print("Sent verification email")
                        return (jsonify({
                            "Success": True,
                            "Reason": "Sent verification email",
                            "errorCode": 0
                        }))
                    else:
                        print(f"failed to send | {result.split('*')[1]}")
                        return (jsonify({
                            "Success": False,
                            "Reason": "Email Error",
                            "SpecificError": str(result.split('*')[1]),
                            "errorCode": 3
                        }))
                else:
                    return (jsonify({
                        "Success": False,
                        "Reason": "Already registered email",
                        "errorCode": 1
                    }))
            else:
                print("invalid")
                return (jsonify({
                    "Success": False,
                    "Reason": "Invalid Email",
                    "errorCode": 2
                }))


        # homepage (EASYCAPTCHAS)
        @app.route('/easycaptcha/home', methods=['GET'])
        @is_google
        def easyhomepage():

            return ("homepage")


        # logout (EASYCAPTCHAS)
        @app.route('/api/v1/logout', methods=['GET'])
        def logouteasycaptcha():

            session.clear()
            return redirect("/login")


        # adscend verification
        @app.route('/login/adscend.html', methods=['GET'])
        def adscendverificationfle5467456723():
            return ("Adscend Media verification")


        # login (EASYCAPTCHAS)
        @app.route('/api/v1/login')
        def logineasycaptcha():
            authorization_url, state = flow.authorization_url()
            session["state"] = state
            return redirect(authorization_url)


        # devtest api
        @app.route('/devtest')
        def devtestapi():
            rule = request.url_rule
            if 'easycaptchas' in rule.rule:
                return (f"accessed from rule {rule.rule} | found easycaptchas")
            else:
                return (f"accessed from rule {rule.rule} | failed to find easycaptchas")


        # google oauth callback (EASYCAPTCHAS)
        @app.route('/easycaptcha/callback', methods=['GET'])
        def easycapcallbackgoogleoauth():
            r = json.loads(requests.post("https://oauth2.googleapis.com/token", data={
                "client_id": "884745994664-mbddq041oos76tdppmfhm0fo7fa07unj.apps.googleusercontent.com",
                "client_secret": "wvzYUvZw6aEzeYuDA6S2aoCX",
                "code": request.args.get("code"),
                "grant_type": "authorization_code",
                "redirect_uri": "https://easycaptchas.coolbux.live/easycaptcha/callback"
            }).text)
            try:
                access_token = r["access_token"]
            except Exception:
                return ("Failed to register, please try re-signup")
            r = json.loads(
                requests.get(f"https://www.googleapis.com/oauth2/v2/userinfo?access_token={access_token}").text)
            email = str(r["email"])
            # check if already registered via md5 hash (irrevisible for security standards)
            result = hashlib.md5(email.encode())
            try:
                e = open(f"Database\\EasyCaptcha\\Reg\\{result.hexdigest()}")
            except Exception:
                print("unregistered")
                try:
                    gname = str(r["name"])
                except Exception:
                    gname = "Easy Captchas User"

                # register user with information

                # send welcome email
                resultwhocares = SendMail(senderaddress="easycaptchas@gmail.com", senderpassword="Ashton2101!",
                                          reciever=email, body=f'''Hello, {gname}. 

                                                Thanks for registering with us on EasyCaptchas! To get started, deposit some credits or redeem a GiftCard to start getting Captchas solved.

                                                - EasyCaptchas Team''', subject="👋 Welcome to EasyCaptchas")

                # register user with id
                key = str(secrets.token_hex(32))

                # register as ar-registered
                e = open(f"Database\\EasyCaptcha\\Reg\\{result.hexdigest()}", "w")
                e.write(key)
                e.close()

                # store cookie
                session[
                    ".EASY-CAPTCHA-SECURITY"] = "WARNING-DO-NOT-SHARE-THIS-WITH-ANYONE-OR-THEY-WILL-HAVE-ACCESS-TO-YOUR-ACCOUNT_|" + str(
                    key)
                res = make_response(render_template("home.html"))
                res.set_cookie('.EASY-CAPTCHA-SECURITY',
                               value=f"WARNING-DO-NOT-SHARE-THIS-WITH-ANYONE-OR-THEY-WILL-HAVE-ACCESS-TO-YOUR-ACCOUNT_|{key}",
                               domain='easycaptchas.coolbux.live')
                profile = str(r["picture"])

                # create api key

                capikey = open(f"Database\\Captcha\\{key}", "w")
                capikey.write("0")
                capikey.close()

                # create tsolved

                capikey = open(f"Database\\Captcha\\TotalSolved\\{key}", "w")
                capikey.write("0")
                capikey.close()

                # create pend
                capikey = open(f"Database\\Captcha\\CEpnd\\{key}", "w")
                capikey.write("0")
                capikey.close()

                # store cookie
                e = open(f"Database\\EasyCaptcha\\Reg\\Cookie\\{key}", "w")
                if gname == "Easy Captchas User":
                    gname = f"EasyCaptchas_{random.randrange(0, 999)}"
                e.write(f"{key}*{profile}*{gname}")
                e.close()
                return res
            else:
                print("setting cookie in session")
                session[
                    ".EASY-CAPTCHA-SECURITY"] = "WARNING-DO-NOT-SHARE-THIS-WITH-ANYONE-OR-THEY-WILL-HAVE-ACCESS-TO-YOUR-ACCOUNT_|" + str(
                    open(f"Database\\EasyCaptcha\\Reg\\{result.hexdigest()}").read())
                res = make_response(render_template("home.html"))
                res.set_cookie('.EASY-CAPTCHA-SECURITY',
                               value=f"WARNING-DO-NOT-SHARE-THIS-WITH-ANYONE-OR-THEY-WILL-HAVE-ACCESS-TO-YOUR-ACCOUNT_|" + str(
                                   open(f'Database\\EasyCaptcha\\Reg\\{result.hexdigest()}').read()),
                               domain='easycaptchas.coolbux.live')
                return res


        # calculate reward based on token
        @app.route('/dashboard', methods=["GET"])
        def dashboardpage():
            return send_from_directory('', 'easycaptchahome.html')


        # calculate reward based on token
        @app.route('/stats', methods=["GET"])
        def statendview():
            return send_from_directory('', 'stats.html')


        # calculate reward based on token
        @limiter.limit("60 per minute")
        @app.route('/api/v1/captcha/reward/<token>', methods=["GET"])
        def captchaapireward(token):
            return ("down")
            vtoken = requests.post("https://roblox-api.arkoselabs.com/fc/gfct/",
                                   {"token": token, "sid": "ap-southeast-1", "render_type": "canvas",
                                    "data[status]": "init", "analytics_tier": 40, "lang": "en"})
            capresp = json.loads(vtoken.text)
            print(capresp)
            if capresp["challengeURL"] == '001':
                print("invalid captcha provided for reawrd")
                return (jsonify({
                    "Success": False,
                    "Reason": "Invalid Captcha / Failed to get results"
                }))
            else:
                capwaves = int(capresp["game_data"]["waves"])
                dreward = str(CalculateReward(waves=capwaves))
                difficulty = Difficulty(waves=capwaves)

                return (jsonify({
                    "Success": True,
                    "Reward": str(dreward),
                    "Difficulty": difficulty
                }))


        # spin roulette (InstaRobux)
        @app.route('/instarobux/external/api/spinwheel/<user>', methods=['GET'])
        def instarobuxspin(user):
            lowendprizes = [1, 2, 5]

            # check offer balance (3 offers minimum)

            # if over 3 or = 3 deduct 3
            offerbalance = int(json.loads(requests.get(f"instarobux.gg/api/v1/offerbal/{user}").text)["obal"])
            if offerbalance > 3:
                # send postback to reduce
                requests.get(f"instarobux.gg/api/v1/robal/{user}")
                # spin wheel
                rannum = random.randrange(0, 101)
                if rannum == 1:
                    prize = 100
                    # insert instarobux postback here
                    return ({"Spinned": True,
                             "Prize": str(prize),
                             "Generated": str(rannum)})
                elif rannum > 95:
                    prize = 50
                    # insert instarobux postback here
                    return ({"Spinned": True,
                             "Prize": str(prize),
                             "Generated": str(rannum)})
                else:
                    prize = random.choice(lowendprizes)
                    # insert instarobux postback here
                    return ({"Spinned": True,
                             "Prize": str(prize),
                             "Generated": str(rannum)})


        # Robux Deposits (EASYCAPTCHAS)
        @app.route('/easycaptcha/deposit/robux/create/<user>/<amount>/<apikey>', methods=['GET'])
        def deprobux(user, amount, apikey):
            # ratelimit for only once every 10 seconds
            # check if int
            try:
                int(amount)
            except Exception as e:
                return (jsonify({"Success": False,
                                 "Reason": "Oops! Make sure the amount of robux you entered is an integer and has no characters",
                                 "Specific": e}))
            depositids = [6411264647, 6411265364, 6411265907, 6411266375, 6411266962, 6411267582, 6411267988,
                          6411268417, 6411268826, 6411269219, 6411269569, 6411270018]
            # check previous deposit amounts

            try:
                e234 = open(f"Database\\Predep\\{user}", "r").read().split("\n")
            except Exception:
                if int(amount) < 7:
                    return ({"Success": False,
                             "Reason": f"The minimum deposit amount is R$7"})

                # calculate usd reward
                captchareward = float(amount) * 0.00355
                # create shirt for that cost and store as session for api key
                depositshirt = str(random.choice(depositids))
                # initate cookie session
                session = requests.session()
                account = open("Cookiecu.txt", "r").read()
                cookielogin = requests.cookies.RequestsCookieJar()
                cookielogin.set('.ROBLOSECURITY', account)
                session.cookies = cookielogin

                # get crsf token
                def CreateAuth():
                    authurl = "https://auth.roblox.com/v1/authentication-ticket/"
                    Authpost = session.post(authurl)
                    return Authpost.headers["X-CSRF-TOKEN"]

                try:
                    CRSFToken = CreateAuth()
                except Exception:
                    return ({"Success": False,
                             "Reason": f"Robux Deposits are currently disabled. "})

                resp = session.post(f"https://itemconfiguration.roblox.com/v1/assets/{depositshirt}/update-price",
                                    json={"priceConfiguration": {"priceInRobux": str(amount)}}, headers={
                        'X-CSRF-TOKEN': CRSFToken,
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
                    })
                if resp.status_code == 200:
                    if resp.text == "{}":
                        print(f"successfully listed {depositshirt} for R${amount} (~{captchareward} Credits)")
                        # store under session id
                        sessionid = secrets.token_hex(8)
                        e = open(f"Database\\Robux\\{sessionid}", "w")
                        e.write(f"{user}*{amount}*{apikey}*{captchareward}*{captchareward}")
                        e.close()
                        return ({"Success": True,
                                 "Shirt": f"https://www.roblox.com/catalog/{depositshirt}",
                                 "SessionID": str(sessionid),
                                 "Reward": str(captchareward)})
                    else:
                        print(resp.text)
                        return (jsonify({"Success": False,
                                         "Reason": "Failed to list product",
                                         "Specific": resp.text}))
                else:
                    print(resp.text)
                    return (jsonify({"Success": False,
                                     "Reason": "Failed to list product",
                                     "Specific": resp.text}))
            else:
                for dep in e234:
                    print(dep)
                    if dep == '':
                        dep = "0.07483957371"
                    deposit = float(dep.strip("\n"))
                    if deposit == float(amount):
                        print("already previously deposited this amount! not proceeding with transaction")
                        return ({"Success": True,
                                 "Reason": f"You've already deposited this amount in the past! Make your purchase 1 robux less or higher."})

                if float(amount) < 7:
                    return ({"Success": False,
                             "Reason": f"The minimum deposit amount is R$7"})
                else:

                    # calculate usd reward
                    captchareward = float(amount) * 0.00355
                    # create shirt for that cost and store as session for api key
                    depositshirt = str(random.choice(depositids))
                    # initate cookie session
                    session = requests.session()
                    account = open("Cookiecu.txt", "r").read()
                    cookielogin = requests.cookies.RequestsCookieJar()
                    cookielogin.set('.ROBLOSECURITY', account)
                    session.cookies = cookielogin

                    # get crsf token
                    def CreateAuth():
                        authurl = "https://auth.roblox.com/v1/authentication-ticket/"
                        Authpost = session.post(authurl)
                        return Authpost.headers["X-CSRF-TOKEN"]

                    try:
                        CRSFToken = CreateAuth()
                    except Exception:
                        return ({"Success": False,
                                 "Reason": f"Robux Deposits are currently disabled. "})

                    resp = session.post(f"https://itemconfiguration.roblox.com/v1/assets/{depositshirt}/update-price",
                                        json={"priceConfiguration": {"priceInRobux": str(amount)}}, headers={
                            'X-CSRF-TOKEN': CRSFToken,
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
                        })
                    if resp.status_code == 200:
                        if resp.text == "{}":
                            print(f"successfully listed {depositshirt} for R${amount} (~{captchareward} Credits)")
                            # store under session id
                            sessionid = secrets.token_hex(8)
                            e = open(f"Database\\Robux\\{sessionid}", "w")
                            e.write(f"{user}*{amount}*{apikey}*{captchareward}*{captchareward}")
                            e.close()
                            return ({"Success": True,
                                     "Shirt": f"https://www.roblox.com/catalog/{depositshirt}",
                                     "SessionID": str(sessionid),
                                     "Reward": str(captchareward)})
                        else:
                            print(resp.text)
                            return (jsonify({"Success": False,
                                             "Reason": "Failed to list product",
                                             "Specific": resp.text}))
                    else:
                        print(resp.text)
                        return (jsonify({"Success": False,
                                         "Reason": "Failed to list product",
                                         "Specific": resp.text}))


        # RedeemGiftcard API
        @app.route('/api/v1/redeem/giftcard/<code>/<key>', methods=['GET'])
        @limiter.limit("1/second")
        def redeemgc(code, key):
            print("checking all codes for a match")
            fncount = 0
            redem = False
            amount = 0
            codenme = ""
            lnes34 = open("Database\\EasyCaptchas\\allgc.bin", "r").read().split("\n")

            for codez in lnes34:
                fncount += 1
                if codez.split(":")[0] == code:
                    print("found code! removing")
                    del lnes34[fncount - 1]
                    new_file = open("Database\\EasyCaptchas\\allgc.bin", "w+")
                    for line in lnes34:
                        new_file.write("\n" + line)
                    new_file.close()

                    print("add to their balance")
                    cbal = int(open(f"Database\\Captcha\\{key}", "r").read())
                    cbal += int(codez.split(":")[1])
                    nbel = open(f"Database\\Captcha\\{key}", "w")
                    nbel.write(str(cbal))
                    nbel.close()
                    # log it
                    e = open(f"Database\\GClogs\\gcredeems.bin", "a")
                    e.write(f"{key}:{codez}")
                    e.close()
                    amount += int(str(codez.split(":")[1]))
                    codenme = codez.split(":")[0]
                    redem = True
            if redem == True:
                return (jsonify({"Success": True,
                                 "Amount": f"{amount}",
                                 "Reason": f"Successfully redeemed code {codenme} for ${amount} USD"}))
            else:
                return (jsonify({"Success": False,
                                 "Amount": f"{amount}",
                                 "Reason": f"This code may already be redeemed or isn't valid"}))


        # nv game verification system
        @app.route('/api/v1/verifyrbx/889345sdfdgshsdfhg754w6df7sgshdfg/<user>', methods=['GET'])
        def ngameverifcationdf(user):
            print("checking if registered")
            try:
                e = open(f"Database\\Pays\\{user}", "r").read()
            except Exception:
                return (jsonify({"Reason": "Not registered",
                                 "Success": False}))
            else:
                print("adding to pending verify")
                phrase = secrets.token_hex(16)
                e = open(f"Database\\RBXVerify\\P1\\{user}", "w")
                e.write(str(phrase))
                e.close()
                return (jsonify({"Phrase": phrase,
                                 "Success": True}))


        # isVerifiedAPI
        @app.route('/api/v1/isVerified/<user>', methods=['GET'])
        def isVerifiedrbx(user):
            try:
                e = open(f"Database\\Security\\Done\\{user}", "r").read()
            except Exception:
                return (jsonify({"Verified": False}))
            else:
                return (jsonify({"Verified": True}))


        # set password system
        @app.route('/api/v1/setpass/<pin>/<user>/<phrase>', methods=['GET'])
        def ngameverifcationpass(pin, user, phrase):
            flag = 0
            if len(pin) > 32:
                jfy = {"Success": False,
                       "Reason": "Oops! The maximum password length is 32 characters."}
                return (jsonify(jfy))
            if len(pin) < 6:
                jfy = {"Success": False,
                       "Reason": "Oops! Your password can only have a minimum length of 6 characters."}
                return (jsonify(jfy))

            print("Checking security of pin")

            print("== Password validity checks ==")
            password = str(pin.lower())
            presults = zxcvbn(password)
            if float(presults["score"]) < 2:
                print(presults)
                rsn = presults["feedback"]["warning"]
                suges = presults["feedback"]["suggestions"]
                if len(str(rsn)) < 2:
                    if len(str(suges)) < 2:
                        jfy = {"Success": False,
                               "Reason": f"Oops! Increase your password strength"}
                        return (jsonify(jfy))
                    else:
                        jfy = {"Success": False,
                               "Reason": f"Oops! Increase your password strength; To increase the strength of the password {pin} you can {suges}"}
                        return (jsonify(jfy))
                else:
                    if len(str(suges)) < 2:
                        jfy = {"Success": False,
                               "Reason": f"Oops! Increase your password strength, {rsn}"}
                        return (jsonify(jfy))
                    else:
                        jfy = {"Success": False,
                               "Reason": f"Oops! Increase your password strength, {rsn} | Suggestion {suges}"}
                        return (jsonify(jfy))

            print(f"== Doing Integrity checks ==")
            print("(1/1) > Checking if valid security phrase!")
            prephrase = open(f"Database\\RBXVerify\\P1\\{user}", "r").read()
            if prephrase == phrase:
                print("valid security phrase! removing phrase & continuing")

                os.remove(f"Database\\RBXVerify\\P1\\{user}")
                # verify user here
                e = open(f"Database\\Security\\Done\\{user}", "w")
                e.write(str(pin))
                e.close()
                jfy = {"Success": True,
                       "Reason": f"Your pin {pin} has been setup!",
                       "Pin": str(pin)}
                return (jsonify(jfy))
            else:
                print("invalid phrase")
                jfy = {"Success": False,
                       "Reason": "Oops! Your security phrase is invalid."}
                return (jsonify(jfy))


        @app.route('/easycaptcha/track/robux/deposit/<sessionid>', methods=['GET'])
        def trackrobuxdepid(sessionid):
            print(f'checking sess {sessionid}')
            try:
                sessioninfo = open(f"Database\\Robux\\{sessionid}", "r").read()
            except Exception:
                return (jsonify({"Success": False,
                                 "Reason": "Session doesn't exist",
                                 "Specific": None}))
            else:
                # check for purchased products
                username = sessioninfo.split("*")[0]
                if True == True:
                    print("no purchases made can continue")
                    # check if purchased shirt
                    amount = float(sessioninfo.split("*")[1])
                    apikey = sessioninfo.split("*")[2]
                    capcreditadd = float(sessioninfo.split("*")[3])
                    session = requests.session()
                    cookie = open("Cookiecu.txt", "r").read()
                    cookielogin = requests.cookies.RequestsCookieJar()
                    cookielogin.set('.ROBLOSECURITY', cookie)
                    session.cookies = cookielogin
                    information = json.loads(session.get(
                        f"https://economy.roblox.com/v2/groups/9654562/transactions?cursor=&limit=25&sortOrder=Asc&transactionType=Sale").text)
                    try:
                        tdps = 0
                        tdp = 0
                        dta = information["data"]
                        for key in dta:
                            if key["agent"]["name"].lower() == username.lower():
                                print("Match found! | Checking deposit")

                                deposited = key["currency"]["amount"]
                                if deposited == amount:
                                    tdp += 1
                                    print("deposit match!")
                                else:
                                    print("different deposit amount")

                            else:
                                print("Ignoring, not deposit")
                    except Exception:
                        return (jsonify({"Success": False,
                                         "Amount": "0",
                                         "Reason": "Failed to grab deposits - JSON Parsing issue (ROBLOX API)"}))
                    else:
                        print("json works api parse, checking")
                        if tdp > 0:
                            print("credit match! credit deposit")
                            ckeycredit = float(open(f"Database\\Captcha\\{apikey}", "r").read())
                            ckeycredit += float(capcreditadd)
                            e = open(f"Database\\Captcha\\{apikey}", "w")
                            e.write(str(ckeycredit))
                            e.close()
                            ato = open(f"Database\\Predep\\{username}", "a")
                            ato.write(f"{amount}\n")
                            ato.close()
                            return (jsonify({"Success": True,
                                             "Amount": f"{capcreditadd}",
                                             "Reason": f"You've successfully been credited ${capcreditadd} USD"}))
                        else:
                            return (jsonify({"Success": False,
                                             "Amount": None,
                                             "Reason": f"You haven't purchased the shirt!"}))


        @app.route('/api/v1/easycaptcha/Prioritycosts', methods=['GET'])
        def priocosts():
            # get all in queue
            count = 0
            highcont = 0.0009
            nray = []
            for nln in open("Database\\Captcha\\queue.bin", "r").read().split("\n"):
                if nln == "\n":
                    pass
                else:
                    count += 1
                    nray.append(float(nln.split("*")[1]))
                    if float(nln.split("*")[1]) > highcont:
                        highcont = float(nln.split("*")[1])
            if count > 0:
                print(f"{count} users in queue")
                # get median score
                medium = statistics.median(nray)
                # get lowest
                lowprio = min(nray)
                if count < 5:
                    return (jsonify({
                        "High": highcont,
                        "Medium": medium,
                        "Low": lowprio,
                        "QueueSize": "Small"
                    }))
                elif count > 5:
                    if count > 10:
                        return (jsonify({
                            "High": highcont,
                            "Medium": medium,
                            "Low": lowprio,
                            "QueueSize": "Medium"
                        }))
                    else:
                        if count < 10:
                            return (jsonify({
                                "High": highcont,
                                "Medium": medium,
                                "Low": lowprio,
                                "QueueSize": "SubMedium"
                            }))
                        else:
                            if count > 30:
                                return (jsonify({
                                    "High": highcont,
                                    "Medium": medium,
                                    "Low": lowprio,
                                    "QueueSize": "Large"
                                }))
                            else:
                                return (jsonify({
                                    "High": highcont,
                                    "Medium": medium,
                                    "Low": lowprio,
                                    "QueueSize": "Big"
                                }))

            else:
                return (jsonify({
                    "High": 0.001,
                    "Medium": 0.00095,
                    "Low": 0.0009
                }))


        # == EVENT APIS ==

        # Reward event prize
        @app.route('/api/v1/event/reward/983455675jf4gd8345634435nd7sf8453/<user>/<prize>', methods=['GET'])
        def reventprizereward(user, prize):
            # get prize type
            types = {"25Candy": 0.5, "100Candy": 1, "250Candy": 1.25, "Shaft": 0.75, "Lagoon": 0.75, "Water": 0.75}
            exst = ["25Candy", "100Candy", "250Candy", "Shaft", "Lagoon", "Water"]
            if prize in exst:
                print("prize exists")
                # check if already claimed
            else:
                print("temp ban account for investigation (unauthorized request)")
                e = open(f"Database\\Banned\\{user}", "w")
                e.write(
                    f"{datetime.datetime.today().strftime('%Y-%m-%d')}*(Automated Ban) -> You've automatically been banned for suspicious activity.*(Automated Ban) -> You've automatically been banned for suspicious activity.")
                e.close()
                return (jsonify({"Rewarded": True,
                                 "Prize": None}))


        # reward homer battle
        @app.route('/api/v1/event/sinister/reward/battle/homer/<user>', methods=['GET'])
        def rewarduser(user):
            # check if already done
            try:
                e = open(f"Database\\Event\\Sinister\\HM\\{user}", "r").read()
            except Exception:
                return (jsonify({"Rewarded": False,
                                 "Prize": None,
                                 "Reason": "You've already completed this mission"}))
            else:
                print("checking if already registered")
                try:
                    e = open(f"Database\\Pays\\{user}", "r").read()
                except Exception:
                    print("doesnt exist - registering")
                    resp = json.loads(requests.get(f"https://coolbux.live/register/{user}").text)["Registered"]
                    if resp == True:
                        print("success registering | rewarding")
                        # reward to balance
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        cbal += 1
                        nbal = open(f"Database\\Pays\\{user}", "w")
                        nbal.write(str(cbal))
                        nbal.close()
                        # add to history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Rewarded R$1 | Halloween Event | Beating Homer (Dance Battle)\n")
                        userhistory.close()
                        iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                        # make it so they can't redo
                        e = open(f"Database\\Event\\Sinister\\HM\\{user}", "w")
                        e.write("")
                        e.close()
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/887572473472749609/fepoOX4Kr1HgmQePNfJq8H9jmm3w3jaVZMMh5lolu1OH5LtS-99CQJCaFOk-tPz3Huva",
                            json={
                                "embeds": [
                                    {
                                        "title": f"Rewarded **{user}**!",
                                        "description": f"**{user}** Just got rewarded R$1 for completing a mission",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{user}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Overview: Player Beat homer dance boss."
                                        }
                                    }
                                ]
                            })
                        return (jsonify({"Rewarded": True,
                                         "Prize": 1,
                                         "Reason": "You've already completed this mission",
                                         "New": True}))
                    else:
                        return (jsonify({"Rewarded": False,
                                         "Prize": 1,
                                         "Reason": "Failed to register on coolbux.",
                                         "New": True}))
                else:
                    print("success registering | rewarding")
                    # reward to balance
                    cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                    cbal += 1
                    nbal = open(f"Database\\Pays\\{user}", "w")
                    nbal.write(str(cbal))
                    nbal.close()
                    # add to history
                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Rewarded R$1 | Halloween Event | Beating Homer (Dance Battle)\n")
                    userhistory.close()
                    iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                    # make it so they can't redo
                    e = open(f"Database\\Event\\Sinister\\HM\\{user}", "w")
                    e.write("")
                    e.close()
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/887572473472749609/fepoOX4Kr1HgmQePNfJq8H9jmm3w3jaVZMMh5lolu1OH5LtS-99CQJCaFOk-tPz3Huva",
                        json={
                            "embeds": [
                                {
                                    "title": f"Rewarded **{user}**!",
                                    "description": f"**{user}** Just got rewarded R$1 for completing a mission",
                                    "color": 8519030,
                                    "author": {
                                        "name": f"{user}",
                                        "icon_url": iconauth
                                    },
                                    "footer": {
                                        "text": f"Overview: Player Beat homer dance boss."
                                    }
                                }
                            ]
                        })
                    return (jsonify({"Rewarded": True,
                                     "Prize": 1,
                                     "Reason": "You've already completed this mission",
                                     "New": False}))


        # reward 5 candies
        @app.route('/api/v1/event/sinister/reward/pirate/candies/<user>', methods=['GET'])
        def rdfghewadfghrdusedfgh234r(user):
            # check if already done
            try:
                e = open(f"Database\\Event\\Sinister\\PC5\\{user}", "r").read()
            except Exception:
                # add to rewarded
                e = open(f"Database\\Event\\Sinister\\PC5\\{user}", "w")
                e.write("1")
                e.close()
                print("checking if already registered")
                try:
                    e = open(f"Database\\Pays\\{user}", "r").read()
                except Exception:
                    print("doesnt exist - registering")
                    resp = json.loads(requests.get(f"https://coolbux.live/register/{user}").text)["Registered"]
                    if resp == True:
                        print("success registering | rewarding")
                        # reward to balance
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        cbal += 1
                        nbal = open(f"Database\\Pays\\{user}", "w")
                        nbal.write(str(cbal))
                        nbal.close()

                        # add to history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Rewarded R$1 | Halloween Event | Collected 5 candies\n")
                        userhistory.close()
                        iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/887572473472749609/fepoOX4Kr1HgmQePNfJq8H9jmm3w3jaVZMMh5lolu1OH5LtS-99CQJCaFOk-tPz3Huva",
                            json={
                                "embeds": [
                                    {
                                        "title": f"Rewarded **{user}**!",
                                        "description": f"**{user}** Just got rewarded R$1 for completing a mission",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{user}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Overview: Player collected 5 candies."
                                        }
                                    }
                                ]
                            })
                        return (jsonify({"Rewarded": True,
                                         "Prize": 1,
                                         "Reason": "You've already completed this mission",
                                         "New": True}))
                    else:
                        return (jsonify({"Rewarded": False,
                                         "Prize": 1,
                                         "Reason": "Failed to register on coolbux.",
                                         "New": True}))
                else:
                    print("success registering | rewarding")
                    # reward to balance
                    cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                    cbal += 1
                    nbal = open(f"Database\\Pays\\{user}", "w")
                    nbal.write(str(cbal))
                    nbal.close()
                    # add to history
                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Rewarded R$1 | Halloween Event | Collected 5 candies\n")
                    userhistory.close()
                    iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/887572473472749609/fepoOX4Kr1HgmQePNfJq8H9jmm3w3jaVZMMh5lolu1OH5LtS-99CQJCaFOk-tPz3Huva",
                        json={
                            "embeds": [
                                {
                                    "title": f"Rewarded **{user}**!",
                                    "description": f"**{user}** Just got rewarded R$1 for completing a mission",
                                    "color": 8519030,
                                    "author": {
                                        "name": f"{user}",
                                        "icon_url": iconauth
                                    },
                                    "footer": {
                                        "text": f"Overview: Player collected 5 candies."
                                    }
                                }
                            ]
                        })
                    return (jsonify({"Rewarded": True,
                                     "Prize": 1,
                                     "Reason": "Rewarded Successfully",
                                     "New": False}))
            else:
                return (jsonify({"Rewarded": False,
                                 "Prize": 1,
                                 "Reason": "Already completed",
                                 "New": False}))


        # reward concert
        @app.route('/api/v1/event/sinister/reward/concert/21pilots/<user>', methods=['GET'])
        def rewarduse234r(user):
            # check if already done
            try:
                e = open(f"Database\\Event\\Sinister\\21P\\{user}", "r").read()
            except Exception:
                # add to rewarded
                e = open(f"Database\\Event\\Sinister\\21P\\{user}", "w")
                e.write("1")
                e.close()
                print("checking if already registered")
                try:
                    e = open(f"Database\\Pays\\{user}", "r").read()
                except Exception:
                    print("doesnt exist - registering")
                    resp = json.loads(requests.get(f"https://coolbux.live/register/{user}").text)["Registered"]
                    if resp == True:
                        print("success registering | rewarding")
                        # reward to balance
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        cbal += 1
                        nbal = open(f"Database\\Pays\\{user}", "w")
                        nbal.write(str(cbal))
                        nbal.close()

                        # add to history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Rewarded R$1 | Halloween Event | Participating in Concert\n")
                        userhistory.close()
                        iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/887572473472749609/fepoOX4Kr1HgmQePNfJq8H9jmm3w3jaVZMMh5lolu1OH5LtS-99CQJCaFOk-tPz3Huva",
                            json={
                                "embeds": [
                                    {
                                        "title": f"Rewarded **{user}**!",
                                        "description": f"**{user}** Just got rewarded R$1 for completing a mission",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{user}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Overview: Player completed Concert 1."
                                        }
                                    }
                                ]
                            })
                        return (jsonify({"Rewarded": True,
                                         "Prize": 1,
                                         "Reason": "You've already completed this mission",
                                         "New": True}))
                    else:
                        return (jsonify({"Rewarded": False,
                                         "Prize": 1,
                                         "Reason": "Failed to register on coolbux.",
                                         "New": True}))
                else:
                    print("success registering | rewarding")
                    # reward to balance
                    cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                    cbal += 1
                    nbal = open(f"Database\\Pays\\{user}", "w")
                    nbal.write(str(cbal))
                    nbal.close()
                    # add to history
                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Rewarded R$1 | Halloween Event | Participating in Concert\n")
                    userhistory.close()
                    iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/887572473472749609/fepoOX4Kr1HgmQePNfJq8H9jmm3w3jaVZMMh5lolu1OH5LtS-99CQJCaFOk-tPz3Huva",
                        json={
                            "embeds": [
                                {
                                    "title": f"Rewarded **{user}**!",
                                    "description": f"**{user}** Just got rewarded R$1 for completing a mission",
                                    "color": 8519030,
                                    "author": {
                                        "name": f"{user}",
                                        "icon_url": iconauth
                                    },
                                    "footer": {
                                        "text": f"Overview: Player completed Concert 1."
                                    }
                                }
                            ]
                        })
                    return (jsonify({"Rewarded": True,
                                     "Prize": 1,
                                     "Reason": "Rewarded Successfully",
                                     "New": False}))
            else:
                return (jsonify({"Rewarded": False,
                                 "Prize": 1,
                                 "Reason": "Already completed",
                                 "New": False}))


        # Custom GCINFO Api
        @limiter.limit("5 per minute")
        @app.route('/api/v1/giftcard/info/<gcid>/<user>', methods=['GET'])
        def getcustogcinfo(gcid, user):

            try:
                gcinfo = open(f"Database\\CGC\\{gcid}", "r").read()
            except Exception:
                return (jsonify({"Success": False,
                                 "Reason": "This giftcard doesn't exist!"}))
            else:
                untes = gcinfo.split("*")
                reward = untes[0]
                creator = untes[1]
                return (jsonify({"Success": True,
                                 "Robux": reward,
                                 "Creator": creator}))


        # Custom GCINFO Api
        @limiter.limit("3 per minute")
        @app.route('/api/v3/giftcard/redeem/<gcid>/<user>', methods=['GET'])
        def redeemcustomgc(gcid, user):

            try:
                gcinfo = open(f"Database\\CGC\\{gcid}", "r").read()
            except Exception:
                return (jsonify({"Success": False,
                                 "Reason": "This giftcard doesn't exist or has already been redeemed!"}))

            else:

                    untes = gcinfo.split("*")
                    reward = float(untes[0])
                    creator = untes[1]
                    try:
                        cbal = open(f"Database\\Pays\\{user}", "r").read()
                    except Exception:
                        print("user doesnt exist")
                        return (jsonify({"Success": False,
                                         "Reason": "You aren't registered!"}))
                    else:
                        os.remove(f"Database\\CGC\\{gcid}")
                        newbal = float(cbal) + reward
                        e = open(f"Database\\Pays\\{user}", "w")
                        e.write(str(newbal))
                        e.close()
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Successfully redeemed a giftcard worth R${reward} (From {creator})\n")
                        userhistory.close()
                        userhistory = open(f"Database\\History\\{creator}", "a")
                        userhistory.write(
                            f"{user} has redeemed your giftcard worth R${reward}\n")
                        userhistory.close()
                        return (jsonify({"Success": True,
                                         "Reason": "Successfully redeemed!",
                                         "Balance": str(newbal)}))



        # reward obby
        @app.route('/api/v1/event/sinister/reward/obby/magical/<user>', methods=['GET'])
        def rewarduse2ob(user):
            # check if already done
            try:
                e = open(f"Database\\Event\\Sinister\\OB1\\{user}", "r").read()
            except Exception:
                # add to rewarded
                e = open(f"Database\\Event\\Sinister\\OB1\\{user}", "w")
                e.write("1")
                e.close()
                print("checking if already registered")
                try:
                    e = open(f"Database\\Pays\\{user}", "r").read()
                except Exception:
                    print("doesnt exist - registering")
                    resp = json.loads(requests.get(f"https://coolbux.live/register/{user}").text)["Registered"]
                    if resp == True:
                        print("success registering | rewarding")
                        # reward to balance
                        cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                        cbal += 3
                        nbal = open(f"Database\\Pays\\{user}", "w")
                        nbal.write(str(cbal))
                        nbal.close()

                        # add to history
                        userhistory = open(f"Database\\History\\{user}", "a")
                        userhistory.write(
                            f"Rewarded R$3 | Halloween Event | Completed Obby\n")
                        userhistory.close()
                        iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                        requests.post(
                            "https://ptb.discord.com/api/webhooks/887572473472749609/fepoOX4Kr1HgmQePNfJq8H9jmm3w3jaVZMMh5lolu1OH5LtS-99CQJCaFOk-tPz3Huva",
                            json={
                                "embeds": [
                                    {
                                        "title": f"Rewarded **{user}**!",
                                        "description": f"**{user}** Just got rewarded R$3 for completing a mission",
                                        "color": 8519030,
                                        "author": {
                                            "name": f"{user}",
                                            "icon_url": iconauth
                                        },
                                        "footer": {
                                            "text": f"Overview: Player escaped M3-OB1."
                                        }
                                    }
                                ]
                            })
                        return (jsonify({"Rewarded": True,
                                         "Prize": 3,
                                         "Reason": "You've already completed this mission",
                                         "New": True}))
                    else:
                        return (jsonify({"Rewarded": False,
                                         "Prize": 3,
                                         "Reason": "Failed to register on coolbux.",
                                         "New": True}))
                else:
                    print("success registering | rewarding")
                    # reward to balance
                    cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                    cbal += 3
                    nbal = open(f"Database\\Pays\\{user}", "w")
                    nbal.write(str(cbal))
                    nbal.close()
                    # add to history
                    userhistory = open(f"Database\\History\\{user}", "a")
                    userhistory.write(
                        f"Rewarded R$3 | Halloween Event | Completed Obby\n")
                    userhistory.close()
                    iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                    requests.post(
                        "https://ptb.discord.com/api/webhooks/887572473472749609/fepoOX4Kr1HgmQePNfJq8H9jmm3w3jaVZMMh5lolu1OH5LtS-99CQJCaFOk-tPz3Huva",
                        json={
                            "embeds": [
                                {
                                    "title": f"Rewarded **{user}**!",
                                    "description": f"**{user}** Just got rewarded R$3 for completing a mission",
                                    "color": 8519030,
                                    "author": {
                                        "name": f"{user}",
                                        "icon_url": iconauth
                                    },
                                    "footer": {
                                        "text": f"Overview: Player escaped M3-OB1."
                                    }
                                }
                            ]
                        })
                    return (jsonify({"Rewarded": True,
                                     "Prize": 3,
                                     "Reason": "Rewarded Successfully",
                                     "New": False}))
            else:
                return (jsonify({"Rewarded": False,
                                 "Prize": 3,
                                 "Reason": "Already completed",
                                 "New": False}))


        # decide coinflip winner
        @app.route('/api/v1/coinflip/winner/<creator>/<choice>', methods=['GET'])
        def deccoinflipwin(creator, choice):
            playerhash = secrets.token_hex(16) + uuid.uuid4().hex * int(choice) + creator[::-1]
            casinohash = secrets.token_hex(16) + uuid.uuid4().hex

            random.seed(playerhash + casinohash)
            unshuf = list(playerhash + casinohash)
            random.shuffle(unshuf)
            game_hash = ''.join(unshuf)
            print(f"Player Hash: {playerhash} | Server Hash: {casinohash} | Game Hash: {game_hash}")
            random.seed(game_hash)
            game_result = random.choice(["Bux", "Tix"])
            print(game_result)
            game_id = secrets.token_hex(16)
            e = open(f"Database\\Gamble\\OSF\\{game_id}", "w")
            e.write(f"{playerhash}:{casinohash}")
            e.close()
            serversha = str(hashlib.sha256(casinohash.encode()).hexdigest())
            return (jsonify({
                "Game_ID": game_id,
                "Player_Hash": playerhash,
                "Server_HashSHA256": serversha
            }))


        # show coinflip winner
        @app.route('/api/v1/join/coinflip/<gameid>', methods=['GET'])
        def showcoinflipwin(gameid):
            try:
                ginfo = open(f"Database\\Gamble\\OSF\\{gameid}", "r").read().split(":")
            except Exception:
                return (jsonify({

                    "Success": False,
                    "Reason": "This bet has already been joined"

                }))
            playerhash = ginfo[0]
            serverhash = ginfo[1]
            gamehash = playerhash + serverhash
            random.seed(gamehash)
            game_result = random.choice(["Bux", "Tix"])
            # remove the game
            os.remove(f"Database\\Gamble\\OSF\\{gameid}")
            return (jsonify({

                "Winner": game_result,
                "ServerHash": serverhash,
                "GameHash": gamehash

            }))


        # update player db
        @app.route(
            '/api/v1/player/location/update/<plr>/<ords>/<collected>/<missionval>/<inmission>/<piratem1>/<piratemission>',
            methods=['GET'])
        def updateplayerdb(plr, ords, collected, missionval, inmission, piratem1, piratemission, missiongui):
            e = open(f"Database\\Event\\PlayerDB\\{plr}", "w")
            e.write(f"{ords}:{collected}:{missionval}:{inmission}:{piratem1}:{piratemission}:{missiongui}")
            e.close()
            return (jsonify({"Updated": True}))


        # retrv player db
        @app.route('/api/v1/player/pdb/<user>', methods=['GET'])
        def retrvplayerdb(user):
            try:
                e = open(f"Database\\Event\\PlayerDB\\{user}", "r")
                playerdbinfo = e.read().split(":")
                e.close()
            except Exception:
                return (jsonify({
                    "Success": False
                }))
            else:
                # now return information in json format
                return (jsonify({
                    "Success": True,
                    "Vector3Coords": playerdbinfo[0],
                    "CollectedVal": None

                }))


        # retrv player db (completed missions)
        @app.route('/missions/completed/async/<user>', methods=['GET'])
        def retrvplayerdbmscomp(user):
            m1 = False
            m2 = False
            m3 = False
            m4 = False
            m5 = False
            try:
                e = open(f"Database\\Event\\Sinister\\PC5\\{user}")
            except Exception:
                pass
            else:
                m1 = True

            try:
                e = open(f"Database\\Event\\Sinister\\OB1\\{user}")
            except Exception:
                pass
            else:
                m2 = True

            try:
                e = open(f"Database\\Event\\Sinister\\21P\\{user}")
            except Exception:
                pass
            else:
                m3 = True

            try:
                e = open(f"Database\\Event\\Sinister\\WCART\\{user}")
            except Exception:
                pass
            else:
                m4 = True

            # add m5 check to that mission

            return (jsonify({
                "M1": m1,
                "M2": m2,
                "M3": m3,
                "M4": m4,
                "M5": m5
            }))


        # complete simple obby mission (main game del)
        @app.route('/missions/completed/delev/<user>', methods=['GET'])
        def fdsghplayreerws(user):
            try:
                e = open(f"Database\\Sinister\\temp\\{user}", "r").read()
            except Exception:
                e = open(f"Database\\Sinister\\temp\\{user}", "w")
                e.write("claimed")
                e.close()
                # reward to balance
                cbal = float(open(f"Database\\Pays\\{user}", "r").read())
                cbal += 7
                nbal = open(f"Database\\Pays\\{user}", "w")
                nbal.write(str(cbal))
                nbal.close()
                # add to history
                userhistory = open(f"Database\\History\\{user}", "a")
                userhistory.write(
                    f"Rewarded R$7 | Halloween Event | Completed Obby\n")
                userhistory.close()
                iconauth = open(f"Database\\Headshots\\{user}", "r").read()
                requests.post(
                    "https://ptb.discord.com/api/webhooks/887572473472749609/fepoOX4Kr1HgmQePNfJq8H9jmm3w3jaVZMMh5lolu1OH5LtS-99CQJCaFOk-tPz3Huva",
                    json={
                        "embeds": [
                            {
                                "title": f"Rewarded **{user}**!",
                                "description": f"**{user}** Just got rewarded R$7 for completing the event!",
                                "color": 8519030,
                                "author": {
                                    "name": f"{user}",
                                    "icon_url": iconauth
                                }
                            }
                        ]
                    })


        # get current game
        @app.route('/game', methods=['GET'])
        def getcgame():
            gamelink = open("cgame.txt", "r").read()
            return gamelink

        # analytics api
        @app.route('/api/v1/analytics/<user>/<wall>/<type>/<hash>/<rval>/<secs>', methods=['GET'])
        def recmapi(user, wall, type, hash, rval, secs):
            #check if user exists
            try:
                e = open(f"Database\\Pays\\{user}", "r").read()
            except Exception:
                return("INVALID USER")
            #confirm if the hash is correct or not
            realhash = hashlib.md5(f"{user}{rval}".encode()).hexdigest()
            if realhash != hash:
                return("INVALID HASH") #return OK by default
            else:
                #check wall type
                if type == "wall":
                 if float(secs) > 60:
                     return("TIME TOO HIGH | COUNTED AS 60")
                 #add to json - secs
                 pass
                elif type == "page":
                    if float(secs) > 60:
                        return ("TIME TOO HIGH | COUNTED AS 60")
                    #add to json
                    pass
                else:
                    return("INVALID WALL")

                return("OK")

        # paypal payout api
        @app.route('/api/v1/payout/paypal/<user>/<pin>/<email>', methods=['GET'])
        def paypalpayout(user, pin):

            print("Checking if user has pin enabled")
            try:
                repin = open(f"Database\\Security\\Done\\{user}", "r").read()
            except Exception:
                jfy = {"Paid": False,
                       "Reason": "Oops! You don't have a PIN Setup, you can set your pin up by clicking the button below."}
                return (jsonify(jfy))
            else:
                print("Verifying if pin is correct")
                if repin != pin:
                    jfy = {"Paid": False,
                           "Reason": "Oops! The pin you entered is incorrect."}
                    return (jsonify(jfy))
                else:
                    print(f"Calculating price of crypto of payout...")
                    usr = user
                    amt22 = float(amount)
                    amt = float(amount)
                    payoutat = float(amount)
                    crpayout = payoutat * 0.005
                    print("testing if user exists")
                    try:
                        e = open('Database\\Pays\\' + usr, 'r')
                        e.read()
                    except Exception:
                        print('user doesnt exist')
                        jfy = {"Paid": False,
                               "Reason": "User doesn't exist"}
                        return (jsonify(jfy))
                    else:
                        print("checking if balance negative")
                        balance = int(float(open(f'Database\\Pays\\{usr}', 'r').read()))
                        if balance < 0:
                            print("bad balance")
                            jfy = {"Paid": False,
                                   "Reason": "Your balance is negative!"}
                            return (jsonify(jfy))


                        else:
                            print("checking balance")
                            balance = float(open(f'Database\\Pays\\{usr}', 'r').read())
                            if amt > balance:
                                print("not enough")
                                jfy = {"Paid": False,
                                       "Reason": "You don't have enough robux to payout this amount!"}
                                return (jsonify(jfy))
                            else:
                                if amt >1000:
                                    #create a payment id
                                    paymentid = secrets.token_hex(8)
                                else:
                                    jfy = {"Paid": False,
                                           "Reason": "The minimum payout is R$1,000 for Paypal."}
                                    return (jsonify(jfy))

        # reccomendation api
        @app.route('/api/v1/reccomended/<user>', methods=['GET'])
        def recmapi234(user):
            #get recently done offers
            try:
             recentoffers = open(f"Database\\USRData\\Categories\\{user}", "r").read()
            except Exception:
                return(jsonify({"Success":False,
                                "Reason":"No recent offers completed",
                                "Count":0}))
            else:
                categories = []
                for offertype in recentoffers.split("\n"):
                    category = offertype.split("*|")[0]
                    print(f"Detected offer: {category}")
                    categories.append(category)
                count = 0
                for i in categories:

                    count+=1
                print("Data count:", count)

                reccategory = most_frequent(categories)

                #Get frequently visited offerwalls (Based on time spent on the wall)
                ofrwalltmesraw = json.loads(open(f"Database\\USRData\\WallTimes\\{user}", "r").read())
                highestofferwall = max(ofrwalltmesraw["walls"], key=itemgetter("time"))
                recwall = highestofferwall["name"]
                if count <=5:
                    #not enough data
                    return (jsonify({"Success": False,
                                     "Reason": "Not enough offer data to recommend",
                                     "Count": str(count)}))
                else:
                    if count <10:
                        #give a variety of offers as they may not have a stuck up option yet, but majority should be what they've recently been doing
                        pass
                    elif count >10:
                        if count<20:
                            #give majority offers of what they've been doing
                            pass
                        else:
                            #make all offers what they've been doing
                            pass

                if reccategory != "Survey":
                    return (jsonify({"Success": True,
                                                 "Count": count,
                                                 "Wall": recwall,
                                                 "Category":reccategory,
                                                 "Type":"Server"
                                     }))
                else:
                    #survey reccomender
                    return (jsonify({"Success": True,
                                                 "Count": count,
                                                 "Wall": recwall,
                                                 "Category":reccategory,
                                                 "Type":"Local"
                                     }))



        # ==== BUX MINER APIS ====

        # miner api (version API)
        @app.route('/api/v1/buxminer/version', methods=['GET'])
        def returnversionapi():
            return ("1.0")


        # miner api (Hint)
        @app.route('/api/v1/buxminer/hint', methods=['GET'])
        def returnbuxminerhint():
            hints = ["The longer you keep BUXPrinter open, the more R$ you earn!",
                     "Need help? Join our discord at discord.gg/P68R8ncHvd", "You can use a Nitro Boost every 6 hours.",
                     "A Nitro Noost will last you 1 hour!", "Robux may take a while to get into your balance.",
                     "Closing BUXPrinter will stop you from earning until you reopen it."]
            return (random.choice(hints))


        from gevent.pywsgi import WSGIServer

        http_server = WSGIServer(('185.223.28.77', 443), app, keyfile='private.key.pem',
                                 certfile='domain.cert.pem')
        http_server.serve_forever()
    except Exception as errorcoo:
        print(f"== Error has occured | {errorcoo} | ==")
        pass
