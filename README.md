<p align="center">
    <img src="Brand.png" alt="App Logo" width="289px" height="260px" />
  </p>
  <h1 align="center">Bank Application</h1>
 
  <!-- TABLE OF CONTENTS -->
  <h2 id="table-of-contents">:book: Table of Contents</h2>
  <details open="open">
    <summary>Table of Contents</summary>
    <ol>
      <li><a href="#about-the-project"> ➤ About The Project</a></li>
      <li><a href="#overview"> ➤ Overview</a></li>
      <li><a href="#howtoinstall"> ➤ Overview</a></li>
      <li>
        <a href="#project-files-description"> ➤ Project Files Description</a>
      </li>
      <li><a href="#Role_1"> ➤ Role 1: Manager </a></li>
      <li><a href="#Role_2"> ➤ Role 2: Representative </a></li>
      <li><a href="#Role_3"> ➤ Role 3: Customer </a></li>
      <li><a href="#Credits"> ➤ Credits</a></li>
    </ol>
  </details>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
  <!-- ABOUT THE PROJECT -->
  <h2 id="about-the-project">:pencil: About The Project</h2>
  
  <p align="justify">
    As using Python->PyQt5 and Mysql database of bank managing, banking,
    transactions of accounts and storing them in 3NF database.
  </p>
  
  <ul>
    <li>
      In order to use the roles, 3 panels (customer, representative, bank manager)
      is designed in the interface.
    </li>
    <li>
      All required information is stored in a relational database (MSSQL, MySQL,
      PostgreSQL).
    </li>
    <li>The database is designed with 3NF optimization.</li>
    <li>All performed operations can be viewed via a GUI(Python->PyQt5).</li>
    <li>
      It can be viewed by clicking the Bank icon on the home page of the ER
      design.
    </li>
  </ul>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
  <!-- OVERVIEW -->
  <h2 id="overview">:cloud: Overview</h2>
  
  <p align="justify">
    There are 3 roles in the bank system: customer, representative and bank
    manager. Required identifying information for customers and employees
    (Name-Surname, Telephone No, Citizenship No, Address, E-mail) is stored in the
    database. A customer can have multiple accounts. Accounts can be opened in any
    currency registered in the system (₺ should come by default). Currency
    conversion should be done automatically when necessary in money transfer
    between accounts. The actions performed by the roles are outlined below. All
    these actions must be displayed visually through a designed interface.
  </p>

  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
    <h2 id="howtoinstall">⛓️ How to install</h2>
  
  <p align="justify">
    There are two way to deal with it:
  <ol>
    <li>Build an executable file with Pylance</li>
      <ul>
         <li> Open the location where all the documents are located.</li>
         <li> Click the right button while pressing the Shift key.</li>
         <li> You can see "Open powershell window here" .</li>
         <li> pyinstaller --onefile -w -i .\Brand.png .\_0BankApplication.py</li>
         <li> Run this line of code with Shell.</li>
         <li> You can see executable file in dist folder in that folder</li>
      </ul>
    <li>Run Main(_0BankApplication) file with IDE</li>
   </ol>
  </p>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  <!-- PROJECT FILES DESCRIPTION -->
  <h2 id="project-files-description">📝: Project Files Description</h2>
  
  <ul>
    <li><b>_0BankApplication.py</b> - Where all the main classes.</li>
    <li>
      <b>_1Manager.py</b> - Where manager form implementation generated from
      reading ui file manager.ui.
    </li>
    <li>
      <b>_2Representative.py</b> - Where representative form implementation
      generated from reading ui file representative.ui.
    </li>
    <li>
      <b>_3Customer.py</b> - Where customer form implementation generated from
      reading ui file customer.ui.
    </li>
    <li><b>_4DatabaseConnection.py</b> - MySql Database connection module.</li>
    <li>
      <b>_5Diagram.py</b> - 3NF database ERR diagram form implementation generated
      from reading ui file diagram.ui.
    </li>
    <li>
      <b>_6Login.py</b> - Where Login form implementation generated from reading
      ui file Login.ui.
    </li>
    <li>
      <b>res_rc_rc.py</b> - Where all resources(icons,backgrounds etc.) object
      code module.
    </li>
    <li><b>assets</b> - Where all resources(icons,backgrounds etc.).</li>
  </ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

  <!-- Role_1 -->
  <h2 id="Role_1">:bank: Customers</h2>

  <ul>
    <li>They can withdraw and deposit money from their accounts.</li>
    <li>
      They can open a new account and delete an existing account.
      <ul>
        <li>An account whose balance is not “0” cannot be deleted.</li>
      </ul>
    </li>
    <li>
      They can transfer money between each other.
      <ul>
        <li>
          During inter-account transfers in different currencies, the amount sent
          is automatically converted to the target currency.
        </li>
      </ul>
    </li>
    <li>They can update their information. (Address, Telephone etc.).</li>
    <li>They can transfer money to the bank. (payment of loan debt).</li>
    <li>
      They can request a loan from the bank.
      <ul>
        <li>Loan can only be requested in ₺.</li>
        <li>
          In case the bank approves the loan request, it is divided by the desired
          maturity rate (interest and principal sum) and reflected to the months
          as debt.
        </li>
        <li>
          In monthly summary display, interest and principal paid for loan debt
          payments is displayed separately.
        </li>
        <li>
          If the customer does not pay the entire monthly debt, the remaining debt
          is carried over to the next month by calculating additional interest.
        </li>
        <li>
          Interest and default interest rate are determined by the bank manager.
        </li>
        <li>
          Monthly debt and remaining debt should be displayed separately.
          (Customer can pay all debt at once).
        </li>
        <li>
          In case of early payment, no interest will be charged for the coming
          months.
        </li>
      </ul>
    </li>
    <li>
      They can view their monthly summaries. (Summary of transactions such as
      sending money, withdrawing, paying loan debts in the current month).
    </li>
  </ul>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
  <!-- Role_2 -->
  <h2 id="Role_2">:bank:Bank manager</h2>

  </p>
  <ul>
    <li>
      It can display the general status of the bank (income, expense, profitand
      total balance).
    </li>
    <li>Determines the loan and default interest rate.</li>
    <li>
      Add new currency (Dollar, Euro, Sterling etc.) and update exchange rates.
    </li>
    <li>Determines the loan and default interest rate.</li>
    <li>
      Will be able to determine the salaries of the employees.
      <ul>
        <li>
          There is only one type of employee (client representative). Their salary
          is the same.
        </li>
      </ul>
    </li>
    <li>
      It can display the general status of the bank (income, expense, profit and
      total balance).
    </li>
    <li>
      They Can add customer.
      <ul>
        <li>
          In case a new customer is added to the system, it is assigned to the
          representative with the least number of customers.
        </li>
      </ul>
    </li>
    <li>
      It can view all transactions (withdrawal, deposit and transfer) realized in
      the bank.
    </li>
    <li>
      In case the listed processes are started at the same time, it can analyze
      whether deadlock occurs or not. Deadlock analysis will be explained in a
      separate section.
    </li>
  </ul>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

  <!-- Role_3 -->
  <h2 id="Role_3">:bank:Representative</h2>

  <ul>
    <li>Each customer has a representative.</li>
    <li>
      They can add Customers, delete and edit (deletion and editing operations are
      only valid for their own customers).
    </li>
    <li>
      >They can update their customer information. (Address, Telephone etc.).
    </li>
    <li>
      They can view the general status (income, expense and total balance) of the
      customers they are interested in.
    </li>
    <li>
      The responsibility of opening, deleting accounts and viewing and approving
      credit requests from customers belongs to the representatives.
    </li>
    <li>
      They can view the transactions (withdrawal, deposit and transfer) of the
      customers they are interested in.
    </li>
  </ul>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
  <!-- Deadlock -->
  <h2 id="Deadlock">Deadlock Analysis</h2>
  <p align="center">
    <table width=50% border-collapse= collapse height= 10%>
      <thead>
        <tr>
          <th align="center"><strong>Procedure No</strong></th>
          <th align="center"><strong>Source</strong></th>
          <th align="center"><strong>Target</strong></th>
          <th align="center"><strong>Procedure</strong></th>
          <th align="center"><strong>Balance</strong></th>
          <th align="center"><strong>Source Balance</strong></th>
          <th align="center"><strong>Target Balance</strong></th>
          <th align="center"><strong>Date</strong></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td align="center">1</td>
          <td align="center"><b>Account1</b></td>
          <td align="center"><b>Account2</b></td>
          <td align="center"><b>Money Transfer</b></td>
          <td align="center"><b>100</b></td>
          <td align="center"><b>900</b></td>
          <td align="center"><b>100</b></td>
          <td align="center"><b>04.13.2022</b></td>
        </tr>
        <tr>
          <td align="center">2</td>
          <td align="center"><b>Account1</b></td>
          <td align="center"><b>Bank</b></td>
          <td align="center"><b>Credit payment</b></td>
          <td align="center"><b>150</b></td>
          <td align="center"><b>750</b></td>
          <td align="center"><b>Null</b></td>
          <td align="center"><b>04.13.2022</b></td>
        </tr>
        <tr>
          <td align="center">3</td>
          <td align="center"><b>User1</b></td>
          <td align="center"><b>Account1</b></td>
          <td align="center"><b>Deposit</b></td>
          <td align="center"><b>200</b></td>
          <td align="center"><b>Null</b></td>
          <td align="center"><b>950</b></td>
          <td align="center"><b>04.15.2022</b></td>
        </tr>
        <tr>
          <td align="center">4</td>
          <td align="center"><b>Account2</b></td>
          <td align="center"><b>Account1</b></td>
          <td align="center"><b>Money Transfer</b></td>
          <td align="center"><b>200</b></td>
          <td align="center"><b>900</b></td>
          <td align="center"><b>1150</b></td>
          <td align="center"><b>05.11.2022</b></td>
        </tr>
        <tr>
          <td align="center">5</td>
          <td align="center"><b>Account2</b></td>
          <td align="center"><b>User1</b></td>
          <td align="center"><b>Withdraw</b></td>
          <td align="center"><b>500</b></td>
          <td align="center"><b>400</b></td>
          <td align="center"><b>Null</b></td>
          <td align="center"><b>05.17.2022</b></td>
        </tr>
      </tbody>
    </table>
  </p>
  <p align="center">
    <img
      src="/deadlockanalysis.png"
      alt="Deadlock Schema"
      height="325px"
      width="650px"
    />
  </p>
  <p>
    The target is prevented from transacting during the money transfer. For this
    reason, an account that is receiving money cannot send money. For deadlock
    analysis, it will be assumed that all processes start simultaneously and work
    in parallel. If we want to do deadlock analysis for Table I: As can be seen in
    the figure, transactions 1 and 4 that started at the same time are locking
    each other. The system will return the number of deadlocks and processes with
    deadlocks as output. For example for Table I: Number of deadlocks : 1
    Operations: An output such as (1-4) should be displayed on the interface. In
    case of multiple deadlocks, the output should be shown as in the figure below.
    Number of deadlocks : 3 Transactions: (1-3-4) , (2-7) , (8-9)
  </p>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
  <!-- CREDITS -->
  <h2 id="Credits">:scroll: Credits</h2>
  
[![GitHubBadge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/canthearwhatusay)[![LinkedInBadge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deniz-%C3%B6zcan-4aa4a8162/)
