import os
import shutil
import subprocess
import argparse

def adapt_env_file(name,env_file):
  print("we'll adapt the environment file so the newly created conda environment will be named {}".format(name))
  with open(env_file,'r') as file:
    filedata = file.read()
  # Replace the target string
  filedata = filedata.replace('template', name)
  with open(env_file,'w') as file:
    file.write(filedata)

def adapt_readme_file(readme_file, template_title='template_title', researcher='researcher', topic='topic'):
  print("we'll adapt the readme file so documentation is correctly initiated")
  with open(readme_file,'r') as file:
    filedata = file.read()
  # Replace the target string
  filedata = filedata.replace('researcher', researcher)
  filedata = filedata.replace('template_title', template_title)
  filedata = filedata.replace('topic', topic)
  with open(readme_file,'w') as file:
    file.write(filedata)

def create_conda_env(env_file):
  # 1. verify if conda is installed in the environment
  conda_installed = subprocess.run(['conda','-c'], capture_output=True, text=True, shell=True)
  if(len(conda_installed.stderr)>0):
    print('conda is not installed yet or not in PATH: {}'.format(conda_installed.stderr))
    return 1
  else:
    if('conda' in conda_installed.stdout):
      print('conda installed with version {}'.format(conda_installed))
  # 2. adapt environment file
  repo_name = input("What should be the name for the repository/project? ")
  adapt_env_file(name=repo_name,env_file=env_file)
  # 3. create environment
  create_env = subprocess.run(['conda','env','create','--file','environment.yml'], capture_output=True, text=True, shell=True)
  if(len(create_env.stderr)>0):
    print('something went wrong while creating the environment: {}'.format(conda_installed.stderr))
    return 1
  else:
    print(create_env.stdout)

def create_topic_folder(topic_name, template_dir):
  ''' 
      we'll create a copy of the template directory and adapt the names where needed to the topic name.
      `topic_name` is the new topic which we want to add
      `template_dir` is the **relative** directory from which we'll make the necessary copies and adjustements for the new topic
  '''
  shutil.copytree(template_dir, 'notebooks/{}'.format(topic_name))
  os.sync()
  adapt_readme_file('notebooks/{}/README.md'.format(topic_name),topic=topic_name)
  os.rename('notebooks/{}/topic.ipynb'.format(topic_name),'notebooks/{}/{}.ipynb'.format(topic_name, topic_name))


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--env","-e", help="create conda environment",
                    action="store_true")
    parser.add_argument("--project","-p", nargs=2, action='store', help="set project name and creator name", type=str)
    parser.add_argument("--topic","-t", action='store', help="create topic folder", type=str)
    args = parser.parse_args()

    if args.env:
        create_conda_env('environment.yml')
    if len(args.project) == 2:
        adapt_readme_file('README.md',template_title=args.project[0],researcher=args.project[1])
    if len(args.topic) == 1:
        create_topic_folder(args.topic[0],'notebooks/template')


