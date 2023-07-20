# R-KORUJA-API-LAMDA-HELLOWORLD

Segredos do repositório do GitHub
Depois de configurar o ambiente da AWS, crie os segredos de ação para as credenciais de segurança da AWS no repositório GitHub (Configurações do repositório -> Segredos e variáveis ​​-> Ações -> Novo segredo do repositório):

Para a função lambda:

AWS_LAMBDA_FUNCTION_NAME: nome da função Lambda

AWS_REGION: região da Função Lambda e do s3

AWS_USER_ACCESS_KEY_ID: ID da chave de acesso para credencial de usuário da Função Lambda

AWS_USER_SECRET_ACCESS_KEY: chave de acesso secreta para credencial de usuário da Função Lambda


Para balde S3:

AWS_S3_BUCKET_NAME: nome do depósito S3

AWS_REGION: região do bucket S3

AWS_USER_ACCESS_KEY_ID: ID da chave de acesso para credencial de usuário da Função Lambda

AWS_USER_SECRET_ACCESS_KEY: chave de acesso secreta para credencial de usuário da Função Lambda