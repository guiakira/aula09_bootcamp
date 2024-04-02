from loguru import logger

logger.add("meu_log.log", level="CRITICAL")

def soma(x,y):
   try:
        soma = x + y
        logger.info(f"Você digitou valores corretos, parabens {soma}")
        return soma
   except:
       logger.critical("Você tem que digitar tipos corretos")


soma(2,7)
soma(2,"3")
