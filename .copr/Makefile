srpm:
    dnf --nogpgcheck -y install rpkg --repofrompath=repo,https://copr-be.cloud.fedoraproject.org/results/cesp/doas/epel-7-x86_64/
    echo '%dist %{nil}' > ~/.rpmmacros
    rpkg srpm --outdir=$(outdir) --spec=$(spec)
