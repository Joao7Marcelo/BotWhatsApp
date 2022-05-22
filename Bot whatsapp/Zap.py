from selenium import webdriver
import time


class Zap:

    def _init_(self):
        #Message to be sent
        self.mensagem = "EX: Good Morning"
        #target group
        self.grupos = ["TEST"]
        options = webdriver.ChromeOptions()
        options.add_argument('en')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def Enviar(self):

        #whatsapp page properties
            # <span dir="auto" title="TESTE" class="_ccCW FqYAR i0jNr">TESTE</span>
            # <div class="_1SEwr">
            # <span data-tested="send" data-icon="send" class="">
        #    
        self.driver.get('http://www.google.com.br/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_1SEwr')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = Zap()
bot.Enviar()