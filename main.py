from datetime import datetime, timezone, timedelta

# Obtém a data e hora atual em UTC
data_hora_utc = datetime.now(timezone.utc)

# Define o fuso horário de Brasília (-3 horas em relação ao UTC)
fuso_horario_brasilia = timezone(timedelta(hours=-3))

# Converte a data e hora para o fuso horário de Brasília
data_hora_brasilia = data_hora_utc.astimezone(fuso_horario_brasilia)

# Formata a data e hora no formato desejado
formato_data_hora = '%d/%m/%Y %H:%M:%S'
data_hora_formatada = data_hora_brasilia.strftime(formato_data_hora)

print("Data e hora atual em Brasília:", data_hora_formatada)
