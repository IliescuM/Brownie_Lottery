1. Users can enter lottery with ETH based on a USD fee
2. An admin will choose when the lottery is over
3. The lottery will select a random winner

How do we want to test this 

1. 'mainnet-for'
2. 'development' with mocks
3. 'test-net'


Enums are one way to create a user -defined type in Solidity. They are explicitly convertible to and from all integer types but implicit conversion is not allowed. The xplicit converison from integer checks at runtime that the value lies inside the range of the enum and causes a Panic error otherwise. Enums require at least one member, and its deafult value when declared is the first member. Enums cannot have more than 256 members.
The data representation is the same as for enums in C: The options are represented by subsequent unsinged integer values starting from 0. 

EX: enum ActionChoices {GoLeft,GoRight,GoStraight, SitStill}
    ActionChoices choice;
    ActionChoices  constant defaultChoice= ActionChoices.GoStraight;