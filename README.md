# PHPUnit_eval-stdin_RCE
(CVE-2017-9841) PHPUnit_eval-stdin_php Remote Code Execution

A code injection vulnerability in PHPUnit, a PHP unit testing framework which part of the Mailchimp , Mailchimp E-Commerce moduels in Drupal 
The vulnerability within the /phpunit/src/Util/PHP/eval-stdin.php file through its use of the php://input wrapper.

    Affected :  PHPUnit 4.8.19 - 4.8.27 , PHPUnit 5.0.10 - 5.6.2
    
    [Vuln path]
    /vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /vendor/phpunit/phpunit/Util/PHP/eval-stdin.php
    /vendor/phpunit/src/Util/PHP/eval-stdin.php
    /vendor/phpunit/Util/PHP/eval-stdin.php
    /phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /phpunit/phpunit/Util/PHP/eval-stdin.php
    /phpunit/src/Util/PHP/eval-stdin.php
    /phpunit/Util/PHP/eval-stdin.php
    /lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php
    /lib/phpunit/phpunit/Util/PHP/eval-stdin.php
    /lib/phpunit/src/Util/PHP/eval-stdin.php
    /lib/phpunit/Util/PHP/eval-stdin.php
    
This script which check the presence or absence of CVE-2017-9841 Vulnerability is based on Python2.

    <Usage>
    
    python PHPUnit_eval-stdin_RCE.py <dst_ip> <dst_port> (user defined port)

    python PHPUnit_eval-stdin_RCE.py <dst_ip> (default : 80/tcp)
