### Dockerfile explanation:

- **pip install --upgrade pip**
    - this is placed first because non-root user cannot access such commands. 
    - But then .. why "non-root user"?
        - It's because using pip with sudo privilege may cause the risk of being hacked and a lot of things. So you cannot do pip install with sudo mode. That's why you need to use "non-root user".
        - Even if you try, you get the following;
          "WARNING: Running pip install with root privileges is generally not a good idea."
<br>
          <br>

- **adduser -D migo**
    - D has been used to avoid passwd input<br><br>
- **COPY --chown=migo:migo requirements.txt requirements.txt**
    - It is to give ownership of the file to user (migo)<br><br>
- **RUN pip install --user -r requirements.txt**
    - Running pip install with the --user flag installs the dependencies for the current user in the .local/bin directory in the user's home directory.<br><br>
- **ENV PATH="home/migo/.local/bin:${PATH}"** 
    - To add path to preexisting PATH<br><br>
- **COPY --chown=migo:migo . .** 
    - To give an ownership to user.  But then... Why duplicate things?
        - It's mainly because by doing so you can avoid unnecessary cache-busting.<br><br>


 

 