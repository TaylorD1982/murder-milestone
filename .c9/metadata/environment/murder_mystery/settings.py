{"filter":false,"title":"settings.py","tooltip":"/murder_mystery/settings.py","undoManager":{"mark":25,"position":25,"stack":[[{"start":{"row":27,"column":17},"end":{"row":27,"column":86},"action":"insert","lines":["'9789e65bcf9840e8a867634f1b3a45a8.vfs.cloud9.us-east-1.amazonaws.com'"],"id":6}],[{"start":{"row":27,"column":18},"end":{"row":27,"column":85},"action":"remove","lines":["9789e65bcf9840e8a867634f1b3a45a8.vfs.cloud9.us-east-1.amazonaws.com"],"id":7},{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":["o"]},{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":["s"]},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"insert","lines":["."]},{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"insert","lines":["e"]},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"insert","lines":["n"]}],[{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"insert","lines":["v"],"id":8},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"insert","lines":["i"]},{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":["r"]},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["o"]},{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"insert","lines":["n"]},{"start":{"row":27,"column":28},"end":{"row":27,"column":29},"action":"insert","lines":["."]},{"start":{"row":27,"column":29},"end":{"row":27,"column":30},"action":"insert","lines":["g"]},{"start":{"row":27,"column":30},"end":{"row":27,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":31},"end":{"row":27,"column":32},"action":"insert","lines":["t"],"id":9}],[{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":["("],"id":10}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"remove","lines":["'"],"id":11}],[{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"remove","lines":["'"],"id":12}],[{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":["C"],"id":13},{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":["9"]},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["_"]},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["H"]}],[{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":["O"],"id":14},{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["T"]}],[{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"remove","lines":["T"],"id":15}],[{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["S"],"id":16},{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"insert","lines":["T"]},{"start":{"row":27,"column":39},"end":{"row":27,"column":40},"action":"insert","lines":["N"]},{"start":{"row":27,"column":40},"end":{"row":27,"column":41},"action":"insert","lines":["A"]},{"start":{"row":27,"column":41},"end":{"row":27,"column":42},"action":"insert","lines":["M"]},{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"insert","lines":["E"]}],[{"start":{"row":27,"column":43},"end":{"row":27,"column":44},"action":"insert","lines":["'"],"id":17}],[{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":["'"],"id":18}],[{"start":{"row":27,"column":45},"end":{"row":27,"column":46},"action":"insert","lines":[")"],"id":19}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":46},"action":"remove","lines":["os.environ.get('C9_HOSTNAME')"],"id":20},{"start":{"row":27,"column":17},"end":{"row":27,"column":86},"action":"insert","lines":["'9789e65bcf9840e8a867634f1b3a45a8.vfs.cloud9.us-east-1.amazonaws.com'"]}],[{"start":{"row":120,"column":23},"end":{"row":121,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":121,"column":0},"end":{"row":122,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":122,"column":0},"end":{"row":122,"column":74},"action":"insert","lines":["MESSAGE_STORAGE = \"django.contrib.messages.storage.session.SessionStorage\""],"id":22}],[{"start":{"row":57,"column":8},"end":{"row":57,"column":19},"action":"remove","lines":["'DIRS': [],"],"id":23},{"start":{"row":57,"column":8},"end":{"row":57,"column":54},"action":"insert","lines":["'DIRS': [os.path.join(BASE_DIR, 'templates')],"]}],[{"start":{"row":122,"column":74},"end":{"row":123,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":123,"column":0},"end":{"row":124,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":124,"column":0},"end":{"row":124,"column":64},"action":"insert","lines":["EMAIL_BACKEND = \"django.core.mail.backends.console.EmailBackend\""],"id":25}],[{"start":{"row":124,"column":0},"end":{"row":124,"column":1},"action":"insert","lines":["#"],"id":26}],[{"start":{"row":125,"column":0},"end":{"row":126,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":126,"column":0},"end":{"row":130,"column":16},"action":"insert","lines":["EMAIL_USE_TLS = True","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_HOST_USER = os.environ.get(\"EMAIL_ADDRESS\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")","EMAIL_PORT = 587"],"id":28}],[{"start":{"row":124,"column":0},"end":{"row":124,"column":1},"action":"remove","lines":["#"],"id":29}],[{"start":{"row":130,"column":16},"end":{"row":131,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":131,"column":0},"end":{"row":132,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":132,"column":0},"end":{"row":135,"column":1},"action":"insert","lines":["AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.EmailAuth'","]"],"id":31}]]},"ace":{"folds":[],"scrolltop":1427,"scrollleft":0,"selection":{"start":{"row":135,"column":1},"end":{"row":135,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1586078771021,"hash":"b141fe5aea987898453c1cca5eb369702806dcab"}