import io
import logging
import re
from typing import Dict, List, Optional

import paramiko

from .vault import VaultClient

ANSI_ESCAPE = re.compile(
    r"""
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
""",
    re.VERBOSE,
)
class SSHClient:
    def __init__(self,*,ssh_username: str,ssh_private_key_vault_path: str,
@classmethod
    def new(cls,*,ssh_username: str,
        ssh_private_key_vault_path: str,
        vault_client: VaultClient,
    ) -> "SSHClient":
        client = cls(
            ssh_username=ssh_username,
            ssh_private_key_vault_path=ssh_private_key_vault_path,
        )
        client.ssh_private_key = vault_client.read(ssh_private_key_vault_path)
        return client
def run(
        self, *, commands: List[str], node_ip: str, redact: Optional[List[str]] = None
    ) -> None:
        ssh_private_key_obj = io.StringIO(self.ssh_private_key)
        with paramiko.SSHClient() as ssh_client:
            log.info(f"Connecting via SSH to {node_ip}")
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(
                hostname=node_ip,
                username=self.ssh_username,
                pkey=paramiko.RSAKey.from_private_key(ssh_private_key_obj),
            )
log.info(f"Connected via SSH to {node_ip}")
            for command in commands:
                cleaned = command
                for redaction in redact or []:
                    cleaned = cleaned.replace(redaction, "****")
                log.info(f"Running: {cleaned}")
                _, stdout, _ = ssh_client.exec_command(command, get_pty=True)
                for line in iter(lambda: stdout.readline(2048), ""):
                    cleaned = ANSI_ESCAPE.sub("", line.rstrip())
                    log.info(f"Stdout: {cleaned}")
@classmethod
    def from_params(cls, vault_client: VaultClient, params: Dict[str, str]):
        return cls.new(
            ssh_username=params["ssh_username"],
            ssh_private_key_vault_path=params["ssh_private_key_vault_path"],
            vault_client=vault_client,
        )
