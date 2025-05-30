import antihash_manager

HASH_FOLDER_PATH = "/home/mrfufl4ik/pycharm/FLauncherClient/modpacks/frogpvp/client/mods"
HASH_FILE = "/home/mrfufl4ik/pycharm/FLauncherClient/modpacks/frogpvp/client/versions/hash_sums.sha1"

if __name__ == "__main__":
    hashes = antihash_manager.create_hashes(HASH_FOLDER_PATH)
    for hash in hashes: print(hash)
    write_hashes = []
    for hash in hashes:
        write_hashes.append(hash + "\n")
    if len(write_hashes) > 0:
        open(HASH_FILE, "w").writelines(write_hashes)