from dotenv import dotenv_values


def mergeEnvs(firstEnv: dict, secondEnv: dict) -> dict:
    result = firstEnv.copy()
    result.update(secondEnv)
    return result


env: dict = mergeEnvs(
    dotenv_values('.env'),
    dotenv_values('.env.local'),
)
