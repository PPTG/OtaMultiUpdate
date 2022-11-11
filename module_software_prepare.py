import os

class PrepareAnotherFiles:
    @staticmethod
    def hex(hex_file, hex_secound_file, hexmodulenumber):
        if not os.path.exists('Preparing'):
            os.makedirs('Preparing')
        mainfile = open(hex_file, 'rb').read()
        createdfile = open('Preparing/' + 'Compact_' + hexmodulenumber + '.bin', 'wb')
        sentence = 'Compact_' + hexmodulenumber
        createdfile.write(mainfile.replace(bytes(hex_secound_file.encode('utf-8')), bytes(sentence.encode('utf-8'))))
        createdfile.close()
