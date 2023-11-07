from selenium import webdriver

# Especifique o caminho para o WebDriver do Opera
opera_driver_path = 'caminho/para/o/operadriver.exe'

# Inicialize o driver do Opera
driver = webdriver.Opera(executable_path=opera_driver_path)

# Abra uma página da web
driver.get('https://twitter.com/home')

# Realize ações automatizadas, como clicar em elementos, preencher formulários, etc.
# Por exemplo: driver.find_element_by_id('element_id').click()

# Encerre o driver quando terminar
driver.quit()
