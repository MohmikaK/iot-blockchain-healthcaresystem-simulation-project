const hre = require("hardhat");

async function main() {
  // Retrieve the ContractFactory for the IoTData contract
  const IoTDataFactory = await hre.ethers.getContractFactory("HealthcareSensors");

  // Deploy the contract with initial parameters if any
  const iotData = await IoTDataFactory.deploy();
  

  console.log("Contract deployed");
  console.log("Registration Number: 21BCT0027");
}

// Execute the deployment script
main()
  .then(() => process.exit(0)) // Exit process if deployment was successful
  .catch((error) => {
    console.error(error); // Log any errors
    process.exit(1); // Exit process with failure code
  });
