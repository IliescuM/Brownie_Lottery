from brownie import (
    network,
    config,
    accounts,
    MockV3Aggregator,
    Contract,
    VRFCoordinatorMock,
    LinkToken,
)

FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local1"]


def get_account(index=None, id=None):
    # accounts[0]
    # accounts.add("env")
    # accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENV
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])


contract_to_mock = {
    "eth_usd_price_feed": MockV3Aggregator,
    "vrf_coordinator": VRFCoordinatorMock,
    "link_token": LinkToken,
}


def get_contract(contract_name):
    """This funciton will grab the contract addreses from the brownie
    config if defined, otherwise, it will deploy a mock version of that
    contract, and return that mock contract

         Args:
            contract_name(string)

        Returns:
            brownie.network.contract.ProjectContract : The most recently deployed
            versionf of this contract.
    """
    contract_type = contract_to_mock[contract_name]

    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        if len(contract_type) <= 0:
            # MockV3Aggregator.lenght
            deploy_mocks()
        contract = contract_type[-1]
        # MockV3Aggregator[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        # address
        # abi
        contract = Contract.from_abi(
            contract_type.name, contract_address, contract_type.abi
        )
        # MockV3Aggregator.Abi
    return contract


DECIMALS = 8
STARTING_PRICE = 200000000000


def deploy_mocks(decimals=DECIMALS, init_value=STARTING_PRICE):
    account = get_account()
    MockV3Aggregator.deploy(decimals, init_value, {"from": account})
    link_token = LinkToken.deploy({"from": account})
    VRFCoordinatorMock.deploy(link_token.address, {"from": account})
    print("Deployed!")
