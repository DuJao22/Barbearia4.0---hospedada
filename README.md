# 💈 Sistema de Barbearia

Sistema completo de gerenciamento para barbearias com agendamentos, controle de funcionários e programa de fidelidade.

## 🚀 Funcionalidades

### 👨‍💼 **Administrador**
- Dashboard com estatísticas completas
- Gerenciamento de funcionários
- Controle de clientes
- Configurações da barbearia
- Confirmação de agendamentos

### ✂️ **Funcionário**
- Agenda pessoal
- Controle de atendimentos
- Visualização de ganhos

### 👤 **Cliente**
- Agendamento online
- Programa de fidelidade
- Histórico de cortes
- Pagamento via PIX

## 🛠️ Tecnologias

- **Backend**: Python Flask
- **Banco de dados**: SQLiteCloud
- **Frontend**: HTML5, CSS3, JavaScript
- **Ícones**: Lucide Icons
- **Hospedagem**: Compatível com Heroku, Railway, etc.

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd sistema-barbearia
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
DATABASE_URL=sqlitecloud://chtue0yuhk.g1.sqlite.cloud:8860/barbearia.db?apikey=oa2q9I4Zp3I2L8e15StCNLZPgGH8N2Yd89NB7ofW6Lo
SECRET_KEY=sua_chave_secreta_aqui
FLASK_ENV=development
```

### 4. Execute a aplicação
```bash
python run.py
```

## 🌐 Deploy

### Heroku
```bash
heroku create nome-da-sua-app
heroku config:set DATABASE_URL=sua_url_do_sqlitecloud
heroku config:set SECRET_KEY=sua_chave_secreta
git push heroku main
```

### Railway
1. Conecte seu repositório
2. Configure as variáveis de ambiente
3. Deploy automático

## 🔐 Acesso Inicial

**Administrador padrão:**
- Email: `admin@barbearia.com`
- Senha: `admin123`

## 📱 Responsividade

O sistema é totalmente responsivo e funciona em:
- 💻 Desktop (> 1024px)
- 📱 Tablet (768px - 1024px)
- 📱 Mobile (< 768px)

## 🎨 Características

- ✨ Design moderno e elegante
- 🌙 Tema escuro profissional
- 📱 Totalmente responsivo
- ⚡ Performance otimizada
- 🔒 Segurança robusta
- 💳 Integração PIX

## 📞 Suporte

Sistema desenvolvido por **João Layon**

---

© 2025 Sistema de Barbearia. Todos os direitos reservados.