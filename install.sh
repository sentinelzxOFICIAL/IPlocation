declare -A COLORS
COLORS[0]='\033[0;31m'  
COLORS[1]='\033[0;32m'  
COLORS[2]='\033[0;33m'  
COLORS[3]='\033[0;34m'  
COLORS[4]='\033[0;35m'  
COLORS[5]='\033[0;36m'  
COLORS[6]='\033[0;37m'  
COLORS[7]='\033[1;31m'  
COLORS[8]='\033[1;32m'  
COLORS[9]='\033[1;33m'  
COLORS[10]='\033[1;34m'  
COLORS[11]='\033[1;35m'  
COLORS[12]='\033[1;36m'  
COLORS[13]='\033[1;37m'  
NC='\033[0m'             


function display_message() {
    local message="$1"
    local color="${COLORS[$((RANDOM % ${#COLORS[@]}))]}"
    local border="--------------------------------------------------"
    echo -e "${color}${border}${NC}"
    echo -e "${color}# ${message}${NC}"
    echo -e "${color}${border}${NC}"
}


function hacking_animation() {
    local message="$1"
    local chars="/-\|"
    echo -n "$message"
    for i in {1..5}; do
        for (( j=0; j<${#chars}; j++ )); do
            echo -ne "${chars:$j:1}" "\r"
            sleep 0.1
        done
    done
    echo ""
}

clear

display_message "Iniciando o script..."


hacking_animation "Concedendo permissão de armazenamento"
termux-setup-storage


hacking_animation "Instalando Python"
pkg install python -y > /dev/null 2>&1 && {
    display_message "Python instalado com sucesso!"
}


hacking_animation "Instalando pip"
pkg install python-pip -y > /dev/null 2>&1 && {
    display_message "pip instalado com sucesso!"
}


hacking_animation "Instalando o módulo requests"
pip install requests > /dev/null 2>&1 && {
    display_message "Módulo requests instalado com sucesso!"
}

display_message "Executando o script main.py..."


python main.py

display_message "Instalação e execução concluídas!"