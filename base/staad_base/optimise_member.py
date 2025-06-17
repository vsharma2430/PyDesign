import statistics
from collections import Counter
from typing import Dict, List, Any
from base.staad_base.property import *
from base.staad_base.root import *
from base.staad_base.design import *

def calculate_average(ratios: Dict[str, float]) -> float:
    """
    Calculate the average of critical ratios, excluding outliers using IQR method.
    
    Args:
        ratios: Dictionary of member names and their critical ratios
    
    Returns:
        Average critical ratio after removing outliers
    """
    if not ratios:
        return 0.0
    
    values = list(ratios.values())
    if len(values) < 4:  # Need enough data for meaningful IQR
        return sum(values) / len(values)
    
    # Calculate Q1, Q3, and IQR
    sorted_values = sorted(values)
    q1 = statistics.quantiles(sorted_values, n=4)[0]
    q3 = statistics.quantiles(sorted_values, n=4)[2]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Filter out outliers
    filtered_values = [v for v in values if lower_bound <= v <= upper_bound]
    
    return sum(filtered_values) / len(filtered_values) if filtered_values else 0.0

def calculate_deviation(ratios: Dict[str, float]) -> float:
    """
    Calculate the standard deviation of critical ratios, excluding outliers using IQR method.
    
    Args:
        ratios: Dictionary of member names and their critical ratios
    
    Returns:
        Standard deviation of critical ratios after removing outliers
    """
    if len(ratios) < 2:
        return 0.0
    
    values = list(ratios.values())
    if len(values) < 4:  # Need enough data for meaningful IQR
        return statistics.stdev(values) if len(values) >= 2 else 0.0
    
    # Calculate Q1, Q3, and IQR
    sorted_values = sorted(values)
    q1 = statistics.quantiles(sorted_values, n=4)[0]
    q3 = statistics.quantiles(sorted_values, n=4)[2]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Filter out outliers
    filtered_values = [v for v in values if lower_bound <= v <= upper_bound]
    
    return statistics.stdev(filtered_values) if len(filtered_values) >= 2 else 0.0

def get_failed_members(ratios: Dict[str, float], threshold: float = 1.0) -> List[str]:
    """
    Get list of members that failed (critical ratio >= threshold)
    
    Args:
        ratios: Dictionary of member names and their critical ratios
        threshold: Failure threshold (default: 1.0)
    
    Returns:
        List of failed member names
    """
    return [(member,ratio) for member, ratio in ratios.items() if ratio >= threshold]

class member_group:
    def __init__(self,Staad_objects:OpenSTAAD_objects, id=None, members=None,exclude_members=None, profiles=None, preference=None,allowable_ratio=0.8):
        self.id = id
        self.geometry = Staad_objects.geometry
        self.property = Staad_objects.property
        self.output = Staad_objects.output

        # Process exclude_members first
        self.exclude_members = unique_list(exclude_members) if exclude_members is not None else []
        
        # Process members and remove any that are in exclude_members
        if members is not None:
            initial_members = unique_list(members)
            self.members = [member for member in initial_members if member not in self.exclude_members]
        else:
            self.members = []

        self.profiles = unique_list(profiles) if profiles is not None else []

        # Get property_id for each member and find the one with highest occurrences
        if self.members:
            property_ids = [get_property_id(self.property, member) for member in self.members]
            most_common = Counter(property_ids).most_common(1)
            self.preference = most_common[0][0] if most_common else get_property_id(self.property, self.members[0])

            property_names = [get_beam_property_name(self.property, member) for member in self.members]
            most_common = Counter(property_names).most_common(1)
            self.profile_name =  most_common[0][0] if most_common else get_beam_property_name(self.property, self.members[0])
        else:
            self.profile_name = None

        self.allowable_ratio = allowable_ratio
        self.results = {}

        # print(f'Created member group "{self.id}" , property {self.preference} with {len(self.members)} members -> {self.members}')
        
    def set_members_property(self,index):
        if(index > -1 and index < len(self.profiles)):
            for member in self.members:
                result = assign_beam_property(self.property,beam_no=member,property_no=self.profiles[index])
            print(f'Assignment of {self.profiles[index]} to {self.members}')

    def set_members_property_initial(self):
        result = []
        if(self.preference is not None):
            for member in self.members:
                result = assign_beam_property(self.property,beam_no=member,property_no=self.preference)
            print(f'Assignment of {self.preference} to {self.members}')
                
    def get_utilization_ratios_for_profile(self,index):
        """
        Process steel design results with statistics
        """
        result = {}
        design_result = get_member_steel_design_results(self.output, self.members)
        
        for member in self.members:
            if member in design_result:
                result[member] = design_result[member]['critical_ratio']  # Fixed key access
        
        # Calculate statistics
        avg = calculate_average(result)
        dev = calculate_deviation(result)
        failed_list = get_failed_members(result,threshold=self.allowable_ratio)
        failed_list.sort(key=lambda x: x[1],reverse=True)
        
        self.results[index] = {
            'profile':self.profiles[index],
            'failed_members': failed_list,  
            'failed': len(failed_list),
            'average': avg,
            'deviation': dev,
            'result': result,
        }

    def get_failed_members_for_profile(self,index):
        if(index in self.results):
            if('failed_members' in self.results[index] and self.results[index]['failed_members'] is not None):
                return [x for (x,y) in  self.results[index]['failed_members']]
        return []
    
    def get_failed_members(self):
        return [x for (x,y) in  self.results['failed_members']]

    def get_utilization_ratios(self):
        """
        Process steel design results with statistics
        """
        result = {}
        design_result = get_member_steel_design_results(self.output, self.members)
        
        for member in self.members:
            if member in design_result:
                result[member] = design_result[member]['critical_ratio']  # Fixed key access
        
        # Calculate statistics
        avg = calculate_average(result)
        dev = calculate_deviation(result)
        failed_list = get_failed_members(result,threshold=self.allowable_ratio)
        
        self.results = {
            'failed_members': failed_list,  
            'failed': len(failed_list),
            'average': avg,
            'deviation': dev,
            'result': result,
        }

    def select_members(self):
        for member in self.members:
            self.geometry.SelectBeam(member)

class optimise_groups:
    def __init__(self):
        self.member_groups = []

    def add(self, group):
        """Add a member_group object to the groups list."""
        if isinstance(group, member_group):
            self.member_groups.append(group)
            return self
        return False
    
    def add_list(self, groups):
        """Add a member_group list object to the groups list."""
        result = []
        for group in groups:
            result.append(self.add(group=group))
        return result

    def list(self):
        """Return the list of member_groups."""
        return self.member_groups

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