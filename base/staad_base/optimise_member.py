from base.staad_base.property import *
from base.staad_base.root import *
from base.staad_base.design import *

class member_group:
    def __init__(self,Staad_objects:OpenSTAAD_objects, id=None, members=None, profiles=None, preference=None):
        self.id = id
        self.property = Staad_objects.property
        self.output = Staad_objects.output
        self.members = members if members is not None else []
        self.profiles = profiles if profiles is not None else []
        self.preference = preference if preference is not None else get_property_id(self.property,self.members[0])
        self.results = {}

        print(f'Created member group "{self.id}" , property {self.preference} with {len(self.members)} members -> {self.members}')
        
    def set_members_property(self,index):
        if(index > -1 and index < len(self.profiles)):
            for member in self.members:
                result = assign_beam_property(self.property,beam_no=member,property_no=self.profiles[index])
            print(f'Assignment of {self.profiles[index]} to {self.members}')

    def set_members_property_initial(self):
        if(self.preference is not None):
            for member in self.members:
                result = assign_beam_property(self.property,beam_no=member,property_no=self.preference)
            print(f'Assignment of {self.preference} to {self.members}')
                
    def get_utilization_ratios(self,index):
        self.results[index] = get_member_steel_design_results(self.output,self.members)

class optimise_groups:
    def __init__(self):
        self.member_groups = []

    def add(self, group):
        """Add a member_group object to the groups list."""
        if isinstance(group, member_group):
            self.member_groups.append(group)
            return self
        return False

    def delete(self, index):
        """Delete a member_group at the specified index."""
        if 0 <= index < len(self.member_groups):
            self.member_groups.pop(index)
            return True
        return False

    def get(self, index):
        """Get a member_group at the specified index."""
        if 0 <= index < len(self.member_groups):
            return self.member_groups[index]
        return None

    def set(self, index, group):
        """Set a member_group at the specified index."""
        if isinstance(group, member_group) and 0 <= index < len(self.member_groups):
            self.member_groups[index] = group
            return True
        return False

    def get_by_id(self, id):
        """Get a member_group by its id."""
        for group in self.member_groups:
            if group.id == id:
                return group
        return None

    def set_by_id(self, id, group):
        """Set a member_group by its id."""
        if isinstance(group, member_group):
            for i, existing_group in enumerate(self.member_groups):
                if existing_group.id == id:
                    self.member_groups[i] = group
                    return True
        return False