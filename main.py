from loguru import logger

logger.add("meu_app.log")

def soma(x,y):
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y



logger.info(soma(2,3))
