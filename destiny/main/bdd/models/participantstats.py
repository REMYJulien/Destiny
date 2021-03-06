from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, BigInteger, Integer, CHAR, SmallInteger

from destiny.main.bdd import Base
from destiny.utils import rep_model

class ParticipantStats(Base):
    __tablename__ = 'participantstats'
    gameId = Column(BigInteger,ForeignKey("matches.gameId"), primary_key=True)
    participantId = Column(SmallInteger, primary_key=True)
    physicalDamageDealt = Column(BigInteger)
    neutralMinionsKilledTeamJungle = Column(SmallInteger)
    magicDamageDealt = Column(BigInteger)
    totalPlayerScore = Column(Integer)
    deaths = Column(SmallInteger)
    win = Column(Boolean)
    neutralMinionsKilledEnemyJungle = Column(SmallInteger)
    largestCriticalStrike = Column(Integer)
    totalDamageDealt = Column(BigInteger)
    magicDamageDealtToChampions = Column(BigInteger)
    visionWardsBoughtInGame = Column(SmallInteger)
    damageDealtToObjectives = Column(BigInteger)
    largestKillingSpree = Column(SmallInteger)
    item1 = Column(Integer)
    quadraKills = Column(SmallInteger)
    totalTimeCrowdControlDealt = Column(Integer)
    longestTimeSpentLiving = Column(Integer)
    wardsKilled = Column(SmallInteger)
    firstTowerAssist = Column(Boolean)
    firstTowerKill = Column(Boolean)
    item2 = Column(Integer)
    item3 = Column(Integer)
    item0 = Column(Integer)
    firstBloodAssist = Column(Boolean)
    visionScore = Column(BigInteger)
    wardsPlaced = Column(SmallInteger)
    item4 = Column(Integer)
    item5 = Column(Integer)
    item6 = Column(Integer)
    turretKills = Column(SmallInteger)
    tripleKills = Column(SmallInteger)
    damageSelfMitigated = Column(BigInteger)
    champLevel = Column(SmallInteger)
    firstInhibitorKill = Column(Boolean)
    goldEarned = Column(Integer)
    magicalDamageTaken = Column(BigInteger)
    kills = Column(SmallInteger)
    doubleKills = Column(SmallInteger)
    trueDamageTaken = Column(BigInteger)
    firstInhibitorAssist = Column(Boolean)
    assists = Column(SmallInteger)
    unrealKills = Column(SmallInteger)
    neutralMinionsKilled = Column(SmallInteger)
    objectivePlayerScore = Column(Integer)
    combatPlayerScore = Column(Integer)
    damageDealtToTurrets = Column(BigInteger)
    physicalDamageDealtToChampions = Column(BigInteger)
    goldSpent = Column(Integer)
    trueDamageDealt = Column(BigInteger)
    trueDamageDealtToChampions = Column(BigInteger)
    pentaKills = Column(SmallInteger)
    totalHeal = Column(BigInteger)
    totalMinionsKilled = Column(SmallInteger)
    firstBloodKill = Column(Boolean)
    largestMultiKill = Column(SmallInteger)
    sightWardsBoughtInGame = Column(SmallInteger)
    totalDamageDealtToChampions = Column(BigInteger)
    totalUnitsHealed = Column(SmallInteger)
    inhibitorKills = Column(SmallInteger)
    totalScoreRank = Column(Integer)
    totalDamageTaken = Column(BigInteger)
    killingSprees = Column(SmallInteger)
    timeCCingOthers = Column(BigInteger)
    physicalDamageTaken = Column(BigInteger)

    def __repr__(self):
        return rep_model(self)
