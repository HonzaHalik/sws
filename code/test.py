button = driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[3]/div/div[{byt}]/div/div/span/h2/a/span')
        button.click()
        time.sleep(sleep)
        #cena
        
        cena_el = driver.find_element(By.XPATH, '//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[1]')
        print(f'cena element: {cena_el}')
        cena = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[1]/strong/span').text)
        cena = re.sub(r'[^0-9]', '', cena)
        print(cena) 
        
        
        poznamka = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[2]/strong/span').text)
        id_zakazky = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[3]/strong/span').text)
        stavba = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[4]/strong/span').text)
        stav_objektu = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[5]/strong/span').text)
        vlasnictvi = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[7]/strong/span').text)
        podlazi = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[8]/strong/span').text)
        uzitna_plocha = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[9]/strong/span[1]').text)
        plocha_podlahova = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[10]/strong/span[1]').text)
        try:
            plocha_zahrady = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[11]/strong/span[1]').text)
        except:
            plocha_zahrady = None
        try:
            balkon = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[1]/li[11]/strong/span[1]').text)
        except:
            balkon = None
        terasa = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[2]/li[1]/strong/span[1]').text)
        
        sklep = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[2]/li[2]/strong/span[1]').text)
        parkovani = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[2]/li[3]/strong/span').text)
        #garaz = str(driver.find_element(By.XPATH, f'').text)
        #garaz = re.sub(r'[^0-9]', '', cena)
        garaz = None
        datum_nastehovani = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[2]/li[5]/strong/span').text)
        voda = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[2]/li[6]/strong/span').text)
        plyn = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[2]/li[7]/strong/span').text)
        telekomunikace = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[2]/li[8]/strong/span').text)
        doprava = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[2]/li[9]/strong/span').text)
        energeticka_narocnost = str(driver.find_element(By.XPATH, f'//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[7]/ul[2]/li[10]/strong/span').text)
        #vytah = str(driver.find_element(By.XPATH, f'').text)
        #vytah = re.sub(r'[^0-9]', '', cena)
        vytah = None
        