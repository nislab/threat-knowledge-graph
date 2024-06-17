# SCA Tool Usage Overview

## Snyk Open Source

1. Fork the repository of the project you wish to scan using GitHub.
2. Visit Snyk Open Source at [Snyk Open Source](https://snyk.io/)
3. Sign up for an account.
4. Add a project from GitHub using the Add projects button on the dashboard.
5. You will be given the option to add personal or organization repositories. Select the repositories you want to add.
6. Your repository will then be imported into the dashboard. Once completed you can view the results of the SCA analysis by clicking on the project name.

![Snyk Output](https://github.com/nislab/threat-knowledge-graph/blob/main/SCA/Images/Snyk-WriteUp-Output.png)

## Red Hat Dependency Analytics

1. The tool is available for multiple IDEs. These instructions are for the Visual Studio Code extension. This requires you to clone the repository locally. It will also require Maven to be installed in case of projects that use Maven in order for the extension to generate the effective pom.
2. Launch Visual Studio Code. Download the extension for Red Hat Dependency Analytics from the Visual Studio Code Extensions tab.
3. After the extension is installed the extension will run automatically whenever the manifest file for the project is opened within the Visual Studio Code environment.

### Note
An issue with running the tool on Windows was faced due to configuring the command for generating the effective pom. Unfortunately, no fix was found other than reinstalling the IDE. **Also ensure that you have run `mvn clean install` for the program.**

![Red Hat Output](https://github.com/nislab/threat-knowledge-graph/blob/main/SCA/Images/RedHat_Sample_Output.png)

## OSV-Scanner

The CLI version of the tool was used on Windows 11.
1. The tool can be installed following the instructions given [here](https://google.github.io/osv-scanner/installation/).
2. Once the tool is installed the various command line arguments can be viewed [here](https://google.github.io/osv-scanner/usage/).
3. From the command line, navigate to the directory that contains the project. After that use the command `osv-scanner -r /path/to/your/dir`
4. The output will be printed in the form of a table to the command window.

![OSV Output](https://github.com/nislab/threat-knowledge-graph/blob/main/SCA/Images/OSV-Writeup-Output.png)

## GitHub Dependabot

1. To use this tool you will need to fork the project on the GitHub website.
2. On the GitHub website, navigate to the Settings tab for the project.
3. Under the Security section on the left, go to the Code Security and Analysis tab. From there enable the Dependencies Graph setting and the Dependabot alerts setting. **Do not enable any other Dependabot setting.**
4. Once enabled, navigate to the Security tab for the project. Click on the Dependabot tab under vulnerability alerts.

![GitHub Output](https://github.com/nislab/threat-knowledge-graph/blob/main/SCA/Images/Dependabot-WriteUp-Output-1.png)
![GitHub Output 2](https://github.com/nislab/threat-knowledge-graph/blob/main/SCA/Images/Dependabot-WriteUp-Output-2.png)
## OWASP Dependency-Check

1. The CLI version of the tool was used on Windows 11. The tool can be downloaded from [here](https://owasp.org/www-project-dependency-check/)
2. The command line arguments for the tool can be viewed [here](https://jeremylong.github.io/DependencyCheck/dependency-check-cli/arguments.html)
3. In order to reproduce the results the following command line argument must be run:
`dependency-check.bat --scan <path to project> —format JSON —output <path to output>`

![OWASP Output](https://github.com/nislab/threat-knowledge-graph/blob/main/SCA/Images/dependency-check-sample.png)



