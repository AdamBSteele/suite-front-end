# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, not_
from sqlalchemy.orm import relationship
from ..extensions import db
from ..utils import get_current_time, diff
from fbone.user.models import User

class Echo(db.Model):

    __tablename__ = 'echo'

    echo_id = Column(db.Integer, primary_key=True)
    user_id = Column(db.Integer,ForeignKey('users.id', onupdate="CASCADE", ondelete="RESTRICT"), nullable=False)
    text = Column(db.Text, nullable=False)
    time = Column(db.Text, nullable=False)
    pub_date = Column(db.DateTime, default=get_current_time)
    publish_user = relationship('User', backref = 'echo', primaryjoin = "Echo.user_id == User.id")
    parent_id = Column(db.Integer,ForeignKey('echo.echo_id', onupdate="CASCADE", ondelete="RESTRICT"), nullable=True)
    root_id = Column(db.Integer,ForeignKey('echo.echo_id', onupdate="CASCADE", ondelete="RESTRICT"), nullable=True)
    response = Column(db.Boolean, nullable=True)
    last_activity = Column(db.DateTime, default=get_current_time)

    def save(self):
        db.session.add(self)
        db.session.commit()


    def get_responses(cls,id):
        query = cls.query.filter(Echo.parent_id == id)
        return query.all()


    def get_all_echos(cls,limit=None,offset=0):
    	query = cls.query.filter(cls.parent_id == None)
    	if limit:
    		query = query.limit(limit)
    	if offset:
    		query = query.offset(offset)
    	return query.all()

    def get_echo_from_user(cls,user,limit=None,offset=0):
        query = cls.query.filter(Echo.user_id == user.id).filter(Echo.parent_id == None)
        if limit:
            query = query.limit(limit)
        if offset:
            query = query.offset(offset)
        return query.all()

    def get_response_echo(cls,user,offset):
        #Get All echos which the user has replied to
        query = cls.query.with_entities(Echo.parent_id).filter_by(user_id = user.id)

        ids = query.all()
        ids = [x.parent_id for x in ids]
        ids = filter(lambda x: x is not None ,ids)
        # Gell all echos whose parent Ids are none i.e they are root echos and specifically the ones which the user hasn't replied too
        return cls.query.filter(Echo.parent_id == None).filter(not_(Echo.echo_id.in_(ids))).order_by(Echo.last_activity.desc()).offset(offset).limit(5).all()
    @classmethod
    def get_all_ordered_by_activity(cls,echo_ids):
        return cls.query.filter(Echo.echo_id.in_(echo_ids)).order_by(Echo.last_activity.desc()).limit(5).all() 

    def get_user_replied_echos(cls,user):
        parent_ids = cls.query.with_entities(Echo.parent_id).filter_by(user_id = user.id).filter(not_(Echo.parent_id == None)).all()
        lis =  [cls.get_by_id(x) for x in parent_ids]
        print lis
        return lis


    @classmethod
    def get_by_id(cls, echo_id):
        return cls.query.filter_by(echo_id=echo_id).first_or_404()