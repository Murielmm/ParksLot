# ParksLot
Gerenciamento de estacionamento - Projeto Matemática Discreta e Lógica - Python

Solicitação:

Voce foi contratado para desenvolver parte do sistema de controle das garagens Park´a´lot. O sistema deve registrar o movimento dos veiculos que entram no prédio para estacionar. O prédio possui um número limitado de vagas (60) que podem ser preenchidas por dois tipos de veículos:

a) motocicletas ( 2 ocupam uma vaga );
b) automoveis ( 1 ocupa uma vaga );

Antes de registrar a ocupação da vaga, deve-se verificar se existem lugares disponíveis para tal. Caso exista, deve-se registrar a placa e modelo do veiculo, o cpf, nome e telefone do dono e a hora da entrada. O registro pode ser em um arquivo de qualquer formato (json, xml, txt).

No momento da saída, é calculado o valor devido, subtraindo a hora da entrada pela hora da saida. Para automóveis, o valor é de 2 reais a primeira hora + 2.50 por hora adicional. Para motocicletas, o valor é de 2 reais a primeira hora + 1.5 por hora adicional. Não existe tolerância mínima. Ao mesmo tempo, deve-se atualizar o total de vagas disponíveis no estacionamento;

O sistema deve permitir uma listagem dos veiculos que estão estacionados de forma ordenada.

A interface pode ser via linha de comando.
