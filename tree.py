
class Member(object):

     def __init__(self, founder):


         self.name = founder
         self.parent = None
         self.children = []

     def __str__(self):
         return self.name

     def add_parent(self, mother):
         self.parent = mother


     def get_parent(self):

         return self.parent


     def is_parent(self, mother):

         return self.parent == mother


     def add_child(self, child):
         self.children.append(child)
         return child in self.children





class Family(object):
    def __init__(self, founder):
        self.names_to_nodes = {}
        self.root = Member(founder)
        self.names_to_nodes[founder] = self.root


    def set_children(self, mother, list_of_children):
        mom_node = self.names_to_nodes[mother]
        for c in list_of_children:
            c_member = Member(c)

            self.names_to_nodes[c] = c_member

            c_member.add_parent(mom_node)

            mom_node.add_child(c_member)

    def is_parent(self, mother, kid):

        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)


    def is_child(self, kid, mother):

        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)


    def cousin(self, a, b):
        a_node = self.names_to_nodes[a]
        b_node = self.names_to_nodes[b]


        def create_branch(node):
            branch = [node]
            parent = node.get_parent()


            while parent:
                branch.append(parent)
                parent = parent.get_parent()
            return branch


        if a_node.name == b_node.name:
            return (-1, 0)
        #elif a_node.is_child(b_node) or b_node.is_child(a_node):
            #return (-1, 0)


        a_branch = create_branch(a_node)
        b_branch = create_branch(b_node)


        b_parent_index = 0
        for a_parent_index, node in enumerate(a_branch):
            try:
                b_parent_index = b_branch.index(node)
                break
            except ValueError:
                pass


        cousin_type = max(a_parent_index, b_parent_index)
        degree_removed = abs(a_parent_index - b_parent_index)
        return (cousin_type, degree_removed)


f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])


words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]


t, r = f.cousin("b", "c")
print("'b' is a", words[t] ,"cousin", "come from 'c'")



t, r = f.cousin("d", "f")
#print("'d' is a", words[t] ,"cousin",  "come from 'f'" n", r, "removed from 'a'")
