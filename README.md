# octal's cp-platforms-api

This project is based on the code from: [SysSn13/all-cp-platforms-API](https://github.com/SysSn13/all-cp-platforms-API)
### Request Format:

```bash
http://cp-api.octalzhihao.top/api/{platform}/{username}
```


Replace {platform} with the name of platform and {username} with the username of the user.

> The username of the Nowcoder is the student id on the personal homepage

---
### Supported Platforms:
- [Codeforces](https://codeforces.com/)
- [Atcoder](https://atcoder.jp/)
- [Nowcoder](https://ac.nowcoder.com/)
---
### Deployment:
The request url may not work in future, so I recommend that you can deploy it on [Vercel](https://vercel.com/) by following these steps easily:
#### 1. Using Heroku web
1. Create a new app on Vercel
2. Fork this repository.
3. Link the forked repo to the new app in the deployment section on Vercel.
#### 2. Using Vercel-cli



1. **Clone the Repository:**

    First, you need to clone the repository from GitHub:

    ```bash
    git clone git@github.com:octal-zhihao/all-cp-platforms-api.git
    ```

    Navigate into the project directory:

    ```bash
    cd all-cp-platforms-api
    ```

2. **Install Vercel CLI:**

    If you haven’t installed the Vercel CLI yet, you can do it globally using npm:

    ```bash
    npm install -g vercel
    ```

3. **Login to Vercel:**

    Log in to your Vercel account using the CLI:

    ```bash
    vercel login
    ```

    This command will open a browser window where you can sign in to your Vercel account.

4. **Deploy the Project:**
    Now, run the following command to initialize the deployment process:
    ```bash
    vercel
    ```

    The Vercel CLI will ask you a series of questions to configure your project:

    - **Link to existing project?** (You can select "No" if this is the first deployment.)
    - **What’s your project’s name?** (You can accept the default name or provide a new one.)
    - **In which scope do you want to deploy it?** (Choose your Vercel account or team.)
    - **Which directory is your code located in?** (Typically the current directory, so press `Enter`.)
    - **Want to override the settings?** (Usually, you can skip this and choose "No".)

    Once this is done, Vercel will automatically build and deploy your project.

5. **Deploy to Production:**

    After configuring the project, you can deploy it to production using:

    ```bash
    vercel --prod
    ```

    This command ensures that your project is deployed to the production environment.

6. **Access Your API:**
    Once the deployment is successful, Vercel will provide a unique URL for your API. You can start making requests using this URL in the format:

    ```sh
    https://your-project-name.vercel.app/api/{platform}/{username}
    ```
   