class TranspositionCipher(object):
    
    def __init__(self, key):
        self.key = key
        
    def encrypt_message(self, message):
        # Gerekli satır sayısını belirleme
        rows = (len(message) + self.key - 1) // self.key
        # Boş 2D liste (matris) oluşturma
        result = [['' for _ in range(self.key)] for _ in range(rows)]
        
        # Mesajı tabloya satır satır yerleştirme
        index = 0
        for i in range(rows):
            for j in range(self.key):
                if index < len(message):
                    result[i][j] = message[index]
                    index += 1

        # Sütun sütun okuyarak şifrelenmiş mesajı oluşturma
        encrypted_msg = ""
        for col in range(self.key):
            for row in range(rows):
                if result[row][col] != '':
                    encrypted_msg += result[row][col]
                    
        return encrypted_msg
    
    def decrypt_message(self, message):
        # Gerekli satır sayısını ve son satırdaki kullanılmayan sütun sayısını hesapla
        rows = (len(message) + self.key - 1) // self.key
        full_cols = len(message) % self.key  # Son satırdaki dolu hücre sayısı
        
        # Boş bir 2D liste (matris) oluşturma
        result_d = [['' for _ in range(self.key)] for _ in range(rows)]
        
        index = 0
        # Şifrelenmiş mesajı sütun sütun tabloya yerleştir
        for col in range(self.key):
            for row in range(rows):
                if row == rows - 1 and col >= full_cols:
                    # Son satırın boş hücrelerini atla
                    continue
                result_d[row][col] = message[index]
                index += 1

        # Tablodan satır satır okuyarak çözülmüş mesajı oluştur
        decrypt_msg = ""
        for row in range(rows):
            for col in range(self.key):
                if result_d[row][col] != '':
                    decrypt_msg += result_d[row][col]
        
        return decrypt_msg

# Test
message = "I confess at these words a shudder passed through me. There was a thrill in the doctor’s voice which showed that he was himself deeply moved by that which he told us. Holmes leaned forward in his excitement and his eyes had the hard, dry glitter which shot from them when he was keenly interested."
key = 12
cipher = TranspositionCipher(key)
encrypted_message = cipher.encrypt_message(message)
print("Encrypted Message:", encrypted_message)

encrypted_messageq = 'asnem trhivt  taotosatihftorru .v naeu sera eogtwrm, nly f . no yelea lyeraed a biedena yrheka  driesaheriy sna ba '
decrypted_message = cipher.decrypt_message(encrypted_messageq)
print("Decrypted Message:", decrypted_message)
