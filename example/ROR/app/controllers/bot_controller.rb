class BotController < ApplicationController

  def index

  end

  def keyboard
    render :json => {
        :type => "text"
    }
  end

  def get_message
    user_key = params[:user_key]
    type = params[:type]
    message = params[:content]

    render :json => {
        :message => {
            :text => message
        }
    }
  end

  def friend_add
    render :json => {
        :success => true
    }
  end

  def friend_out
    render :json => {
        :success => true
    }
  end

  def chat_room_out
    render :json => {
        :success => true
    }
  end
end
