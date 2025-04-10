import yaml

class YAMLLoader:
    def __init__(self):
        self.cfg_file = 'config.yaml'

    def getConfig(self):
        try:
            with open(self.cfg_file, 'r') as f:
                cfg = yaml.safe_load(f)
        except FileNotFoundError:
            raise SystemExit("Error: config.yaml file not found")
        excel = cfg.get('excel', {})
        ms = cfg.get('ms', {})
        aem = cfg.get('aem', {})
        return {
            'excel':excel,
            'ms':ms,
            'aem':aem
        }