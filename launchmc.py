import os
import subprocess
import threading
import consts

from system_manager import is_process_running, kill_process_by_name, is_windows

current_directory = os.getcwd()

def clear_mc_log():
    if os.path.exists(consts.LOG_FILE_NAME): os.remove(consts.LOG_FILE_NAME)


def run_process_log(command):
    with open(consts.LOG_FILE_NAME, 'a') as log_file: subprocess.Popen(command, stdout=log_file, stderr=log_file, shell=True)


def get_config_data(config: dict) -> dict:
    r_cfg = {
        "username"  : config.get("username",    consts.DEFAULT_CONFIG.get("username")),
        "loader"    : config.get("loader",      consts.DEFAULT_CONFIG.get("loader")),
        "version"   : config.get("version",     consts.DEFAULT_CONFIG.get("version")),
        "java_args" : config.get("java_args",   consts.DEFAULT_CONFIG.get("java_args")),
    }
    return r_cfg


def run_mc(config: dict, client_dir: str) -> bool:
    if is_windows():
        process_mc_name = consts.PROCESS_MC_NAME
    else:
        process_mc_name = consts.L_PROCESS_MC_NAME

    if not is_process_running(process_mc_name) or not is_windows():
        new_config = get_config_data(config)

        mc_run_cmd = f"portablemc --main-dir {client_dir} --work-dir {client_dir} start \"{new_config.get("java_args")}\" {new_config.get("loader")}:{new_config.get("version")} -u {new_config.get("username")}"
        try:
            clear_mc_log()
        except:
            print("Ошибка при записи логов! Такое может быть при одновременно запуске функции!")
        thread = threading.Thread(target=run_process_log, args=(mc_run_cmd,))
        thread.start()
        return True
    else:
        return False


def stop_mc() -> bool:
    if is_windows():
        if is_process_running(consts.JAVAW_MC_NAME):
            return kill_process_by_name(consts.JAVAW_MC_NAME)
        if is_process_running(consts.PROCESS_MC_NAME):
            return kill_process_by_name(consts.PROCESS_MC_NAME)
    return None