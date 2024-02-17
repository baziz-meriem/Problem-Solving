from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        #default dict
        domain_dict = defaultdict(int)
        final_list = []

        #parcourir la liste
        for domain in cpdomains:
            #extraire le num 
            occurence,dom = domain.split()
            #extraire la chaine et la subdivisé avec .
            subdomains_list = dom.split('.')
            del dom
            while len(subdomains_list) >=1:
                #join subdom parts 
                subdom = '.'.join(subdomains_list)
                #delete the first entry from the list
                subdomains_list.pop(0)
                #ajouter les subchaines comme clé avec le num comme valeur
                domain_dict[subdom] += int(occurence) 
               
                del subdom

        for dom,occ in domain_dict.items():
            item = str(occ) +' '+ dom
            final_list.append(item)
            del item

        return final_list
        