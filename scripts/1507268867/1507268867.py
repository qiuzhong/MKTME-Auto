
import os
import subprocess
import sys
import time

try:
    host_log = r"C:\Testing\GenericFramework\host.log"
    if os.path.exists(host_log):
        os.remove(host_log)
    time.sleep(1)

    sut_log = r"C:\Testing\GenericFramework\putty.log"
    if os.path.exists(sut_log):
        os.remove(sut_log)
    time.sleep(1)

    test_case = "1507268867"
    count = 0
    steps = 1

    print("\n################################################################")
    command = "C:/Python36/python.exe ./scripts/1507268867/1507268867-1to10-Host.py"
    print("Executing: %s" % command)

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, 
                               stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = process.communicate()
    time.sleep(2)
    print("stdout:")
    print(str(output, encoding='utf-8',errors='ignore'))
    print("stderr:")
    print(str(err, encoding='utf-8',errors='ignore'))
    if process.returncode == 0:
        count = count + 1

    print("\n################################################################")
    if count == steps:
        print("PASS: Successfully Executed Test Case: %s" % test_case)
    else:
        print("FAIL: Execution Failed for Test Case: %s" % test_case)

    print("\n################################################################")
    print("Executing: Cleanup Scenarios")

    print("\n################################################################")
    print("Execution Completed for Cleanup Scenarios")
    print("\n################################################################")

    if count == steps:
        sys.exit(0)
    else:
        sys.exit(1)
except Exception as e:
    print("ERROR: Unable to Execute the Package: due to %s." % e)
    sys.exit(1)
