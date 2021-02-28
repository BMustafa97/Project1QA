---


---

<p>**</p>
<h2 id="project-brief">Project Brief</h2>
<p>The brief set for this project is to create a service-orientated architecture for my application, with the tools, methodologies and technologies that cover all core modules covered during training. The application must be composed of at least four services that work together.</p>
<h3 id="requirements">Requirements</h3>
<p>In order to achieve the brief, the following requirements must be achieved:</p>
<ul>
<li>Trello board</li>
<li>Relational database - with one table.</li>
<li>Clear documentation including design, architecture and risk assessment.</li>
<li>An application fully integrated using the feature branch model into a Version Control System (VCS). The VCS will be built through a CI server (Jenkins) and deployed to a cloud-based virtual machine.</li>
<li>When a change to the code is pushed to the VCS, webhooks must be set up for the CI server to recreate and redeploy the application.</li>
<li>The application must follow the service-orientated architecture which must be deployed using containerisation and an orchestration tool.</li>
<li>Ansible playbook must be made that will provide the environment for the application to run.</li>
<li>A reverse proxy must be set up to make the applciation accessible to the user.</li>
</ul>
<p>**</p>
<h2 id="microservice-architecture">Microservice-architecture</h2>
<p>My project consists of many moving parts, at the very base I have a total of four services which all interact with one another. Service 2 &amp; 3 would both generate a name and slogan from a pre-populated string, randomly. Service 4 would then make requests to both API’s and consolidate this new information which would then be requested by Service 1. Service 1 would then interact with the user and provide them with their desired output as well as persist data to a database so the User could access said data.<br>
Behind all of this Jenkins, Ansible, Docker Swarm/Compose and NGINX are all automating various tasks. Credit to Jenkins for being the centre point to this complex architecture.</p>
<h2 id="my-strategy">My Strategy</h2>
<p>I used an iterative method by simply creating a functional app at first with successful tests, then moving on to enable it’s dockerised capabilities through Dockerfiles and a docker-compose.yaml.  I then incorporated the use of Jenkins to build the various steps of Testing, Building and Deploying at that stage. Then I configured VM’s via Ansible and an NGINX load-balancer.</p>
<p>**</p>
<h2 id="project-management">Project Management</h2>
<h2 id="cicd-pipeline">CI/CD Pipeline</h2>
<h2 id="jenkins-pipeline">Jenkins Pipeline</h2>
<h2 id="testing">Testing</h2>
<h2 id="risk-assessment">Risk Assessment</h2>
<p>Improvements<br>
…</p>

