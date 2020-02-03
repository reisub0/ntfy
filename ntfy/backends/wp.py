#!/usr/bin/env python3
import requests

# Wirepusher Module for ntfy
def notify(**kwargs):
    """
    kwargs contains retcode if using ntfy done or ntfy shell-integration
    and all options in your backend's section of the config
    """
    kwargs['type'] = kwargs.get('type', 'ntfy')
    resp = requests.get('https://wirepusher.com/send', params=kwargs)
    resp.raise_for_status()
