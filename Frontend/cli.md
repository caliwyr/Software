# CLI

https://github.com/aws/aws-cli/

```
aws [options] <command> <subcommand> [parameters]
```

```
aws s3 cp --profile pangolin s3://yes-pangolin/db-backup/$file ./
```

- --profile

## Installation

**macOS**

v1: https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html
v2: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html

The AWS CLI version 2 has no dependencies on other software packages. It has a self-contained, embedded copy of all dependencies included in the installer. You no longer need to install and maintain Python to use the AWS CLI.

To install for all users using the macOS command line

```
cd ~/Downloads/
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /

$ which aws
$ aws --version
```

**Linux**

https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html

```
sudo apt install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

## Credential

```
cat ~/.aws/credentials
```

In credentials, there are multiple profiles.

```
[default]
aws_access_key_id = key-id
aws_secret_access_key = key

[profile-yes]
aws_access_key_id = key-id
aws_secret_access_key = key
```

## Config

```
cat ~/.aws/config
```

In config, there are multiple profiles.

```
[default]
output = json

[profile-yes]
output = json
```

```
aws configure
```

## Profile

## Uninstalling

Uninstalling
To uninstall the AWS CLI version 2, run the following commands, substituting the paths you used to install.

Find the folder that contains the symlinks to the main program and the completer.

```
$ which aws
/usr/local/bin/aws
```

Use that information to find the installation folder that the symlinks point to.

```
$ ls -l /usr/local/bin/aws
lrwxrwxrwx 1 ec2-user ec2-user 49 Oct 22 09:49 /usr/local/bin/aws -> /usr/local/aws-cli/aws
```

Now delete the two symlinks in the first folder. If your user account already has write permission to these folders, you don't need to use sudo.

```
$ sudo rm /usr/local/bin/aws
$ sudo rm /usr/local/bin/aws_completer
```

Finally, you can delete the main installation folder. Use sudo to gain write access to the /usr/local folder.

```
$ sudo rm -rf /usr/local/aws-cli
```
