         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!

# Description
Kode latihan python untuk kelas IDJAK118


# How to integrate cloud 9 with github

<img width="733" height="433" alt="Pasted Graphic 1" src="https://github.com/user-attachments/assets/2d5f90cd-3e3a-4ec0-8349-f13e1126be29" />

1. Create .ssh folder in root folder.
   ```
   mkdir .ssh
   ```
   
2. Generate an SSH key pair named "github". You can customize the name as you like.
   ```
   ssh-keygen -t ed25519 -C "zavfake@gmail.com" -f /home/ec2-user/environment/.ssh/github
   ```
   
3. Create .gitignore file and fill with the code below. Remember: We shouldn't share the private key to everyone. Keeping the key secret on our machine is a must!!
   ```
   .ssh/
   .c9/
   ```
   
4. Create ssh with custom key path. (Repeat this step whenever you start the machine again)
   ```
   eval "$(ssh-agent -s)"
   ssh-add .ssh/github
   ```

5. Init new local git. By default, the new repository will place your code in the "master" branch.
   ```
   git init
   ```
6. Create & checkout to new branch named "main". Remember, when you open the github, the default branch is main, so we should follow this rule.
   ```
   git checkout -b main
   ```

7. Test pulling the code from GitHub
   ```
   git pull origin main
   ```
   
   If you get the error "unrelated history," do this:
   ```
   git pull origin main --allow-unrelated-histories
   ```

8. Sync your code from local git to the GitHub
   ```
   git push origin main --force
   ```

9. Check your uploaded code in GitHub. Happy coding! If you encounter any issues, please drop your question in the whatsapp group and I will answer as soon as possible 😊❤️💡
   
