"""
POP
----------

TIME IS RUNNING OUT. You have been given a task to implement a code deciphering program otherwise the whole world will go POP!

You are going to be given a code with length 3 * N where N will be < 100000. This code will contain only P (capital p) and O (capital o).

You need to find whether or not it is possible to partition the code into several disjoint subsequences. All of these subsequences are the string POP

A string S is a subsequence of string S1 if S can be obtained from S1 by deletion of several (possibly zero) characters.

If it is possible to partition the code into several POP strings then return Yes otherwise return No if it is impossible!

For example. The code POPOPP will return YES (since we form the first POP using the first 2 characters and the last character and then the remaining characters form another POP)

The code POP will return yes. The code PPOOPP will return Yes. The code PPPOOOPOP will return NO. The code POOOPP will return NO. The code OPP will return NO. 


Constraints - 

The code will be at most length 3 * N where N < 100000.

You are guaranteed to get a string filled with only capital O's and capital P's. If String is empty then return NO

Good luck!


"""


class Pop:

    def __init__(self):
        pass

    def pop(self, code: str) -> str:
        """
        This function is where you decypher the code before its too late and world goes pop!
        :param code : The string consisting of P's and O's which you need to decypher
        :return: Yes or No depending if the code can be partitioned into several disjoint subesequences equal to "POP"
        """
        # impoosible situations
        if code == "" or code.count("O") * 2 != code.count("P"):
            return "NO"

        # need to work out if P O and Ps are in right order to make POPs
        # check to make sure enough PO and then Ps
        p = 0
        po = 0
        for letter in code:
            if letter == "P":
                p += 1
            elif letter == "O":
                if p < 1:
                    return "NO"
                po += 1
                p -= 1
        
        if po != p:
            return "NO"
        
        # check if Ps are after POs
        i = 0
        j = len(code) - 1
        open_pop = False
        while i < len(code) and j > 0:
            if code[i] == 'p':
                open_pop = True
                i += 1
            elif True:
                break
        
        return "YES"