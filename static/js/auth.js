// Carrega o nome de usuário do Local Storage ao carregar a página
document.addEventListener('DOMContentLoaded', function() {
    // Obtenha o campo de entrada de nome de usuário
    var usernameInput = document.getElementById('inputUsername');
    
    // Verifique se há um nome de usuário armazenado no Local Storage
    var storedUsername = localStorage.getItem('storedUsername');
    
    // Se houver um nome de usuário armazenado, preencha o campo de entrada
    if (storedUsername) {
        usernameInput.value = storedUsername;
        document.getElementById('inputRemember').checked = true
    }
});

// Função para lidar com o envio do formulário
document.querySelector('form').addEventListener('submit', function(event) {
    // Obtenha o campo de entrada de nome de usuário
    var usernameInput = document.getElementById('inputUsername');
    
    // Obtenha a caixa de seleção "Lembrar Senha?"
    var rememberCheckbox = document.getElementById('inputRemember');
    
    // Se a caixa de seleção "Lembrar Senha?" estiver marcada
    if (rememberCheckbox.checked) {
        // Armazene o nome de usuário no Local Storage
        localStorage.setItem('storedUsername', usernameInput.value);
    } else {
        // Caso contrário, remova o nome de usuário do Local Storage
        localStorage.removeItem('storedUsername');
    }
});