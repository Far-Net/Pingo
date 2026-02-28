from os import system
from colorama import init, Style, Fore
from sys import stdout
from time import sleep
from pyfiglet import figlet_format


def carregando():
    for i in range(3):
        for chars in ['*', '&', '#', '+']:
            stdout.write(Style.BRIGHT + Fore.WHITE + '\rCarregando ' + chars.ljust(4))
            stdout.flush()
            sleep(0.3)

init(autoreset = True)

def pingo():

        #INICIANDO
        system('clear')
        banner = figlet_format('PINGO!', font = 'lean')
        print(Style.BRIGHT + Fore.GREEN + banner)
        print('')

        continuar = input('| Deseja continuar? (s/n): ').strip()
        while continuar == '':
            print(Style.BRIGHT + Fore.RED + '[ ERRO FATAL ]')
            continuar = input('| Deseja continuar? (s/n): ').strip()

        if continuar == 'sim' or continuar == 'ss' or continuar == 's':
            print('')
            print(Style.BRIGHT + Fore.CYAN + '[ INICIANDO ]')
            carregando()
            system('clear')

            print(Style.RESET_ALL + '-'*70)
            print('')

            #ENDEREÇO WEB
            web = input('| Indique um endereço web -> ').strip()

            while web == web.upper() or web == '':
                print('')
                print(Style.BRIGHT + Fore.RED + '[ ERRO FATAL (endereço não especificado...) ]')
                print('')
                web = input('| Indique um endereço web -> ').strip()

            while not web.endswith('.com'):
                print('')
                print(Style.BRIGHT + Fore.RED + '[ ERRO FATAL (o endereço web não possui .com) ]')
                print('')
                web = input('| Indique um endereço web -> ').strip()


            #CONTAGEM DE PACOTES
            while True:
                try:
                    contagem = int(input('| Quantos pacotes deseja mandar para {}? '.format(Style.BRIGHT + Fore.BLUE + web)))
                    break

                    while contagem == '':
                        print('')
                        print(Style.BRIGHT + Fore.RED + '[ ERRO FATAL (número de pacotes não especificado...) ]')
                        print('')
                        contagem = int(input('| Quantos pacotes deseja mandar para {}? '.format(Style.BRIGHT + Fore.BLUE + web)))
                        break

                except ValueError:
                    print('')
                    print(Style.BRIGHT + Fore.RED + '[ ERRO (a contagem de pacotes não suporta letras ou pacotes vazios...) ]')
                    print('')

            if contagem == 66:
                print('')
                print(Style.BRIGHT + Fore.MAGENTA + '[ EXECUTE ORDER 66 ]')
                sleep(3)

            elif contagem > 20:
                print('')
                print(Fore.RED + '[!]', 'MODO MASSIVO, ATIVANDO QUIET MODE')
                sleep(5)

            system('clear')
            print(Style.RESET_ALL + '-'*70) #DEIXANDO AS LINHAS BRANCAS
            print('')

            carregando()

            system('clear')
            print(Style.RESET_ALL + ' CHECANDO '.center(100, '-'))
            print('')

            #SAÍDA DE DADOS ATRIBUÍDOS ACIMA
            print('| Endereço web -> {}'.format(Style.BRIGHT + Fore.GREEN + web))
            if contagem == 66:
                print('| Quantidade de pacotes -> {}'.format(Style.BRIGHT + Fore.MAGENTA + str(contagem)))
            else:
                print('| Quantidade de pacotes -> {}'.format(Style.BRIGHT + Fore.GREEN + str(contagem)))


            print('')
            print('-'*100)
            print('')

            #PING
            if contagem > 20:
                system('ping -c {} -i 0.01 -q {}'.format(contagem, web))
            else:
                system('ping -c {} {}'.format(contagem, web))

            print('')
            print('-'*100)
            print('')

            #TEMPO DE ENVIO
            while True:
                tempo = str(input('| Qunto foi o tempo de envio de pacotes? (time): ')).strip()
                if tempo == '':
                    print(Style.BRIGHT + Fore.YELLOW + '> TEMPO INDEFINIDO')
                    break
                try:
                    tempo_float = float(tempo)
                    if float(tempo_float) < 20:
                        print(Style.BRIGHT + Fore.CYAN + '> Conexão ótima')
                        break
                    elif float(tempo_float) >= 20 and tempo_float <= 50:
                        print(Style.BRIGHT + Fore.GREEN + '> Conexão boa')
                        break
                    elif float(tempo_float) >= 50 and tempo_float <= 100:
                        print(Style.BRIGHT + Fore.YELLOW + '> Conexão aceitável')
                        break
                    elif float(tempo_float) >= 150:
                        print(Style.BRIGHT + Fore.RED + '> Conexão ruim')
                        break
                except ValueError:
                        print('')
                        print(Style.BRIGHT + Fore.RED + '< VALOR INVÁLIDO >')
                        print('')

            print('')

            #PACOTES PERDIDOS
            while True:
                pacote_los = str(input('| Quantos pacotes foram perdidos? (packet loss): ')).strip()

                if pacote_los == '':
                    print(Style.BRIGHT + Fore.YELLOW + '> PACOTES INDEFINIDOS')
                    break
                try:
                    if int(pacote_los) > 0:
                        print(Style.BRIGHT + Fore.RED + '> Instabilidade na rede')
                        break
                    else:
                        print(Style.BRIGHT + Fore.GREEN + '> A rede não apresenta instabilidades')
                        break
                except ValueError:
                    print('')
                    print(Style.BRIGHT + Fore.RED + '< VALOR INVÁLIDO >')
                    print('')

            print('')
            print('-'*100)
            print('')

            #RELATORIO
            relatiorio = input('| Gostaria de ver o relatório? (s/n) ').strip()
            if relatiorio == 's' or relatiorio == 'ss' or relatiorio == 'sim':
                print('')
                print(Style.BRIGHT + Fore.MAGENTA + '[ INICIANDO RELATÓRIO ]')
                carregando()
                system('clear')

                print(Style.RESET_ALL + ' RELATÓRIO '.center(40, '-'))
                print('')

                print('| Endereço web alvo -> {}'.format(Style.BRIGHT + Fore.GREEN + web))
                if contagem == 66:
                    print('| Pacotes enviados -> {}'.format(Style.BRIGHT + Fore.MAGENTA + str(contagem)))
                else:
                    print('| Pacotes enviados -> {}'.format(Style.BRIGHT + Fore.GREEN + str(contagem)))

                tempo_relatorio = str(tempo)

                if tempo_relatorio == '':
                    print(Style.BRIGHT + Fore.YELLOW + '> TEMPO INDEFINIDO')
                else:
                    tempo_relatorio_float = float(tempo_relatorio)

                    if float(tempo_relatorio_float < 20):
                        print('| Tempo -> {}ms, Conexão ótima'.format(Style.BRIGHT + Fore.CYAN + str(tempo_relatorio_float)))
                    elif float(tempo_relatorio_float >= 20 and tempo_relatorio_float <= 50):
                        print('| Tempo -> {}ms, Conexão boa'.format(Style.BRIGHT + Fore.GREEN + str(tempo_relatorio_float)))
                    elif float(tempo_relatorio_float >= 50 and tempo_relatorio_float <= 100):
                        print('| Tempo -> {}ms, Conexão aceitável'.format(Style.BRIGHT + Fore.YELLOW + str(tempo_relatorio_float)))
                    elif float(tempo_relatorio_float > 150):
                        print('| Tempo -> {}ms, Conexão ruim'.format(Style.BRIGHT + Fore.RED + str(tempo_relatorio_float)))

                pacote_relatorio = str(pacote_los)

                if pacote_relatorio == '':
                    print(Style.BRIGHT + Fore.YELLOW + '> PACOTES INDEFINIDOS')
                else:
                    pacote_relatorio_int = int(pacote_relatorio)
                    if pacote_relatorio_int > 0:
                        print('| Pacotes perdids -> {}, Rede instável'.format(Style.BRIGHT + Fore.RED + str(pacote_relatorio_int)))
                    else:
                        print('| Pacotes perdidos -> {}, Rede estável'.format(Style.BRIGHT + Fore.GREEN + str(pacote_los)))

                print('')
                print('-'*40)

            #LOOP
            reset = input('| Quer recomeçar? (s/n): ').strip()
            if reset == 's' or reset == 'ss' or reset == 'sim':
                print('')
                carregando()
                system('clear')
                pingo()
            else:
                print('')
                print(Style.BRIGHT + Fore.RED + '[ SAINDO ]')
                carregando()
                system('clear')
        else:
            print('')
            print(Style.BRIGHT + Fore.RED + '[ FECHANDO ]')
            carregando()
            system('clear')
pingo()

print(Style.BRIGHT + Fore.WHITE + '''

                              ++##@@@@@@@@@@@@@@##--
                          @@@@@@@@@@@@::@@::@@@@@@@@@@##
                      @@@@@@##      MM@@@@::        ##@@@@mm
                    @@@@@@        @@@@@@@@@@@@@@        ##@@##
                  @@@@            ##@@@@@@@@@@##          --@@@@
                @@@@            ::@@@@@@@@@@@@MM              @@@@
              @@@@  ::      ::@@@@@@@@@@@@@@@@@@@@@@          ..@@##
            @@@@  mm@@MM  @@@@@@@@@@--      --@@@@@@@@@@  MM@@  @@@@--
            @@@@  @@@@@@@@@@@@@@@@@@        ++@@@@@@@@@@##@@@@@@++@@@@
          ##@@@@@@@@@@@@@@@@@@@@@@@@MM      ##@@@@@@@@@@@@@@@@@@@@##@@mm
          @@##  @@@@@@@@@@@@MM@@@@@@@@      @@@@@@@@  MM@@@@@@@@@@  @@@@
        ++@@  ##@@@@@@@@##    MM@@@@@@      @@@@@@      ##@@@@@@@@##..@@
        ##@@  @@@@@@@@@@        @@..                      @@@@@@@@@@  @@mm
        @@@@      @@@@@@                                  @@@@MM      @@##
        @@mm      @@@@@@@@                            ##@@@@@@##      @@@@
        @@        @@@@@@@@@@@@MM                  ##@@@@@@@@@@@@      @@@@
        @@        @@@@@@@@@@@@mm                  @@@@@@@@@@@@@@      @@@@
        @@        @@@@@@@@@@@@MM                  ##@@@@@@@@@@@@      @@@@
        @@@@      ##@@@@MM                              ::@@@@##      @@@@
        @@@@      ##@@@@                                  @@@@MM      @@##
        ##@@  @@@@@@@@@@        @@--          @@@@      ..@@@@@@@@@@  @@++
        --@@  MM@@@@@@@@##    mm@@@@@@      @@@@@@mm    @@@@@@@@@@::--@@
          @@##  @@@@@@@@@@@@MM@@@@@@##      @@@@@@@@MM@@@@@@@@@@@@  @@@@
          ##@@@@@@@@@@@@@@@@@@@@@@@@MM      MM@@@@@@@@@@@@@@@@@@@@@@@@..
            @@@@  @@@@@@@@@@@@@@@@@@          @@@@@@@@@@##@@@@@@..@@@@
            mm@@mm  @@    MM@@@@@@@@##......##@@@@@@@@mm  MM@@  ##@@
              ##@@            ##@@@@@@@@@@@@@@@@@@@@          ::@@@@
                @@@@..            ##@@@@@@@@@@MM            ::@@##
                  @@@@mm          @@@@@@@@@@@@MM          ##@@##
                    ##@@##        @@@@@@@@@@@@@@        @@@@@@
                      ::@@@@@@..        @@..      --@@@@@@
                          mm@@@@@@@@@@##@@@@@@@@@@@@@@..
                                mm##@@@@@@@@@@##++
''')
print(Style.BRIGHT + Fore.RED + 'ALL FOR THE EMPIRE')
sleep(2)
system('clear')
