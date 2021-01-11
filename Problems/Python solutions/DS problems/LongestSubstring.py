import numpy as np

class Solution:
    
    def get_pal_len(self, str_in, ind, type):
        #Represents the palindrome of the type "appa" and "amma"
        if(type!=2):
            if(type==0):
                count = 0
                ind_dec = ind
            #Represents the palindrome of the type "madam"
            else:
                count = 1
                ind_dec = ind - 1
            ind_inc = ind + 1
            while(str_in[ind_dec] == str_in[ind_inc]):
                ind_dec = ind_dec - 1
                ind_inc = ind_inc + 1
                count = count + 2
                if(ind_dec<0 or ind_inc>len(str_in)-1):
                    break
        else:
            count = 1
        return count
    
    def get_type_ind(self, str_in, start_ind):
        str_in = ' ' + str_in + '\0'
        out_type = 0
        out_ind = 0
        is_final = False
        for i in range(start_ind, len(str_in)-1):
            if(str_in[i] == str_in[i+1]):
                # Represents the case where the palindrome match is like ("amma" or "appa")
                if(str_in[i] != str_in[i+2]):
                    out_type = 0
                    out_ind = i-1
                else:
                    j = i+2
                    while(str_in[i] == str_in[j]):
                        j = j+1
                    out_ind = int((i + ((j-1-i)/2)) - 1)
                    if(((j-1-i)%2) == 0):
                        out_type = 1
                    else:
                        out_type = 0
                break
            elif(str_in[i-1] == str_in[i+1]):
                # Represents the case where the palindrome match is like ("madam")
                out_type = 1
                out_ind = i-1
                break
            else:
                # Represents the case where the palindrome match is not found
                out_type = 2
                out_ind = 0
            if(i==len(str_in)-2):
                is_final = True
        return (out_type, out_ind, is_final)
    
    def backtrack_get_pal(self, str_in, pal_ind, pal_len, pal_type):
        if(pal_type == 0):
            ind_dec = pal_ind
            out_str = ""
        else:
            ind_dec = pal_ind - 1
            out_str = str_in[pal_ind]
        ind_inc = pal_ind + 1
        pal_type = 0
        for i in range(int(pal_len / 2)):
            out_str = str_in[ind_dec] + out_str + str_in[ind_inc]
            ind_dec = ind_dec - 1
            ind_inc = ind_inc + 1
        return out_str
    
    def longestPalindrome(self, str_in: str) -> str:
        index = 0
        max_len = 0
        pal_ind = 0
        temp_count = 0
        is_final = False
        pal_str = ""
        pal_type = 0
        if(str_in != ""):
            while(is_final == False):
                out_type, out_ind, is_final = self.get_type_ind(str_in, index)
                temp_count = self.get_pal_len(str_in, out_ind, out_type)
                if(temp_count > max_len):
                    max_len = temp_count
                    pal_ind = out_ind
                    pal_type = out_type
                index = out_ind + 2
            pal_str = self.backtrack_get_pal(str_in, pal_ind, max_len, pal_type)
        else:
            pal_str = str_in
        return pal_str