# paddle
Um sistema administrativo da federação mineira de tênis de mesa

# Sprint Planning

**1 - Como administrador, quero cadastrar atleta: Incluir Nome, Data de Nascimento (calcular idade), federado ou não, categorias, pontuação, posição rankings, histórico de presenças. - Bruno**
a. Projetar e criar tabelas.
b. Criar conexão com o banco de dados.
c. Desenvolver formulário de cadastro.
d. Implementar cadastro e atualização de atleta.
e. Limitar permissão.

**2 - Como usuário comum ou administrador, quero fazer login - Bruno**
a. Criar formulário de login no front-end
b. Projetar query de usuário no banco de dados
c. Desenvolver sistema de autenticação no back-end
d. Criar página de perfil
e. Desenvolver método de logout

**3 - Como administrador, quero publicar informes na página inicial - Bárbara**
a. Desenvolver a página inicial.
b. Instalar banco de dados, projetar e criar tabelas.
c. Desenvolver tela para publicar informes.
d. Implementar cadastro, atualização e exclusão de informe.

**4 - Como usuário comum, quero pesquisar atleta - Bárbara**
a. Criar página com formulário de pesquisa e exibição dos atletas
b. Projetar query de pesquisa ao banco de dados
c. Desenvolver sistema no back-end que retorna os resultados
d. Criar tabela que apresenta resultados

**5 - Como administrador, quero criar campeonato - Isadora**
a. Projetar e desenvolver tabelas.
b. Criar formulário de criação de campeonato.
c. Desenvolver back-end e esquema de classificação para as etapas do campeonato.
d. Criar página para visualização do campeonato.

**6 - Como atleta ou adm, quero fazer inscrição em um campeonato - Lucas**
a.Página de seleção de campeonatos disponíveis e criação de query correspondente
b. Opção de requerer inscrição em um campeonato selecionado e criação de query correspondente
c. Opção do administrador de aprovar ou recusar a inscrição de um atleta
d. Criar opção de desinscrição e projetar query correspondente
e. Criar tela de exibição de participantes no campeonato

**7 - Como adm, quero atualizar resultados dos jogos - Luiz**
a. Opção de editar meta informações de cada partida
b. Opção de editar a pontuação de cada partida
c. Sistema de progressão automática de jogadores no campeonato baseado na pontuação da partida e configurações do campeonato

**8 - Como usuário comum, quero visualizar rankings/histórico de campeonatos - Luiz**
a. A partir da aba Campeonatos criar a aba Histórico
b. Colocar todos os torneios organizados em ordem cronológica (do mais recente ao mais antigo)
c. Para cada campeonato, ao clicar, mostrar o ranking do torneio e resultados
d. Criar filtro para pesquisa de campeonatos (data, categoria, participante)
e. A partir da página inicial criar a aba Rankings, com o ranking geral (top 3 em destaque podendo ser visualizado ainda na página inicial)
f. Na aba Rankings criar formulário de pesquisa e mostrar tabela
