#class Solution:
#    def avoidFlood(self, rains: List[int]) -> List[int]:
#        full = set();
#        flood = False;
#        ans = [];
#        
#        def findNextDay(i):
#            for j in range(i, len(rains)):
#                if rains[j] in full:
#                    return rains[j];
#            return 0;
#        
#        for i in range(len(rains)):
#            if rains[i] and rains[i] in full:
#                return [];
#            elif rains[i]:
#                full.add(rains[i]);
#                ans.append(-1);
#            else:
#                nextRain = findNextDay(i)
#                if full and nextRain:
#                    ans.append(nextRain);
#                    full.remove(nextRain);
#                elif full:
#                    ans.append(full.pop());
#                else:
#                    ans.append(1);
#        
#        return ans;
#超时

#不超时的思路:
#
#class Solution:
#    def avoidFlood(self, rains):
#"""
#Given an array of events rains, this program will design an event
#log that will prevent flooding by overflowing lakes, if possible.
#Each event in rains is either a day of rain that fills a single
#lake or a dry day. On a dry day, the program is allowed to dry a
#filled lake or an already dry lake (no effect). If rain falss on
#a filled lake, a flood occurs.
#:param rains: array of events indicating a day of rain on a particular
#              lake or a dry day that allows the program to select
#              which lake becomes dry that day
#:type rains: list[int]
#:return: event log consisting of rainy days indicated by -1 and dry
#         days indicating which lake was dried that day. If a flood
#         occurs, an empty list is returned.
#:rtype: list[int]
#"""
#"""
#Initialize:
#- filled_lakes maps a filled lake with the most recent day that it
#  was filled by rain
#- dry_days is a list of days available to dry a lake so it can be
#  filled by rain again without causing a flood
#- event_log contains a log of events that is returned to the calling
#  program if flooding was prevented or an empty list if flooding
#  could not be prevented.
#"""
#
#rains = [1,2,0,2,3,0,1];
#filled_lakes = {}
#dry_days = []
#event_log = []
#"""
#Process events in rains:
#- If the event was a rainy day on a lake and the lake was already
#  filled by a previous rain, find an available dry day that can
#  be used to dry the lake before it gets rained on again. If there
#  is no dry day available, a flood cannot be prevented.
#- If the event was a rainy day on a dry lake or flooding was
#  prevented, update event_log, filled_lakes, and dry_days.
#- If the event was a dry day, update dry_days with the new day.
#"""
#for day, lake in enumerate(rains):
#    if lake:
#        """
#        Rainy day on lake identified by the variable lake
#        """
#        event_log.append(-1)
#        if lake in filled_lakes:
#            """
#            Lake was previously filled by rain. Look for a valid
#            dry day to dry the lake
#            """
#            last_rainy_day = filled_lakes[lake]
#            valid_dry_day = -1
#            for dry_day in dry_days:
#                if dry_day > last_rainy_day:
#                    valid_dry_day = dry_day
#                    break
#            if valid_dry_day > 0:
#                """
#                Valid dry day found
#                """
#                dry_days.remove(valid_dry_day)
#                filled_lakes[lake] = day
#                event_log[valid_dry_day] = lake
#            else:
#                """
#                Flood could not be prevented
#                """
#                print([])
#        else:
#            """
#            Lake is already dry
#            """
#            filled_lakes[lake] = day
#    else:
#        """
#        Dry day
#        """
#        dry_days.append(day)
#        event_log.append(99999)
#print(event_log)